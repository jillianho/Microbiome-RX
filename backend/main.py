"""
MicrobiomeRx - Drug-Microbiome Interaction Analyzer
FastAPI Backend
"""

import os
import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
from typing import List, Dict, Any, Optional
import logging
import json
import re

from drug_database import (
    DRUG_DATABASE,
    DRUG_CLASS_EFFECTS,
    find_drug,
    get_all_drug_names,
    check_interactions,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="MicrobiomeRx API",
    description="Drug-Microbiome Interaction Analyzer",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# =============================================================================
# Models
# =============================================================================

class AnalyzeRequest(BaseModel):
    drugs: List[str]

class DrugSearchResult(BaseModel):
    name: str
    brand_names: List[str]
    drug_class: str

# =============================================================================
# Endpoints
# =============================================================================

@app.get("/")
async def serve_frontend():
    """Serve the frontend."""
    frontend_path = Path(__file__).parent.parent / "frontend" / "index.html"
    if frontend_path.exists():
        return FileResponse(frontend_path)
    return {"status": "API running", "docs": "/docs"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "drugs_in_database": len(DRUG_DATABASE)}

@app.get("/api/drugs/search")
async def search_drugs(q: str = Query(..., min_length=1)):
    """Search for drugs by name."""
    query = q.lower().strip()
    results = []
    
    for drug_key, drug_info in DRUG_DATABASE.items():
        # Match drug name
        if query in drug_info["drug_name"].lower():
            results.append({
                "name": drug_info["drug_name"],
                "brand_names": drug_info.get("brand_names", []),
                "drug_class": drug_info["drug_class"]
            })
            continue
        
        # Match brand names
        for brand in drug_info.get("brand_names", []):
            if query in brand.lower():
                results.append({
                    "name": drug_info["drug_name"],
                    "brand_names": drug_info.get("brand_names", []),
                    "drug_class": drug_info["drug_class"]
                })
                break
    
    return results[:10]  # Limit to 10 results

@app.get("/api/drugs/all")
async def get_all_drugs():
    """Get all drugs in database."""
    drugs = []
    for drug_key, drug_info in DRUG_DATABASE.items():
        drugs.append({
            "name": drug_info["drug_name"],
            "brand_names": drug_info.get("brand_names", []),
            "drug_class": drug_info["drug_class"],
            "common_uses": drug_info.get("common_uses", [])
        })
    return drugs

@app.get("/api/drug/{drug_name}")
async def get_drug_info(drug_name: str):
    """Get detailed info for a specific drug."""
    drug = find_drug(drug_name)
    if not drug:
        raise HTTPException(status_code=404, detail=f"Drug '{drug_name}' not found")
    return drug

@app.post("/api/analyze")
async def analyze_drugs(request: AnalyzeRequest):
    """Analyze multiple drugs for microbiome interactions."""
    if not request.drugs:
        raise HTTPException(status_code=400, detail="No drugs provided")
    
    # Find all drugs
    found_drugs = []
    not_found = []
    
    for drug_name in request.drugs:
        drug = find_drug(drug_name)
        if drug:
            found_drugs.append(drug)
        else:
            not_found.append(drug_name)
    
    if not found_drugs:
        raise HTTPException(status_code=404, detail=f"No drugs found: {not_found}")
    
    # Aggregate effects
    all_bacteria_decreased = {}
    all_bacteria_increased = {}
    mental_health_concerns = []
    physical_health_concerns = []
    all_recommendations = []
    
    for drug in found_drugs:
        effects = drug.get("microbiome_effects", {})
        
        # Aggregate decreases
        for item in effects.get("decreases", []):
            bacteria = item["bacteria"]
            if bacteria not in all_bacteria_decreased:
                all_bacteria_decreased[bacteria] = {
                    "bacteria": bacteria,
                    "drugs": [],
                    "max_magnitude": item["magnitude"],
                    "mechanisms": []
                }
            all_bacteria_decreased[bacteria]["drugs"].append(drug["drug_name"])
            all_bacteria_decreased[bacteria]["mechanisms"].append(item.get("mechanism", ""))
            # Upgrade magnitude if worse
            if item["magnitude"] == "significant":
                all_bacteria_decreased[bacteria]["max_magnitude"] = "significant"
            elif item["magnitude"] == "moderate" and all_bacteria_decreased[bacteria]["max_magnitude"] == "mild":
                all_bacteria_decreased[bacteria]["max_magnitude"] = "moderate"
        
        # Aggregate increases
        for item in effects.get("increases", []):
            bacteria = item["bacteria"]
            if bacteria not in all_bacteria_increased:
                all_bacteria_increased[bacteria] = {
                    "bacteria": bacteria,
                    "drugs": [],
                    "max_magnitude": item["magnitude"],
                    "mechanisms": []
                }
            all_bacteria_increased[bacteria]["drugs"].append(drug["drug_name"])
            all_bacteria_increased[bacteria]["mechanisms"].append(item.get("mechanism", ""))
        
        # Collect mental health impacts
        mh = drug.get("mental_health_impact", {})
        if mh.get("risk_level") not in ["low", "beneficial", None]:
            mental_health_concerns.append({
                "drug": drug["drug_name"],
                "risk_level": mh.get("risk_level"),
                "effects": mh.get("effects", [])
            })
        
        # Collect physical health impacts
        for effect in drug.get("physical_health_impact", {}).get("effects", []):
            physical_health_concerns.append({
                "drug": drug["drug_name"],
                **effect
            })
        
        # Collect recommendations
        for rec in drug.get("recommendations", []):
            if rec not in all_recommendations:
                all_recommendations.append(rec)
    
    # Check drug-drug interactions
    interactions = check_interactions([d["drug_name"] for d in found_drugs])
    
    # Calculate overall risk
    risk_score = 0
    for drug in found_drugs:
        mh = drug.get("mental_health_impact", {})
        risk_level = mh.get("risk_level", "low")
        if risk_level == "high" or risk_level == "severely negative":
            risk_score += 3
        elif risk_level == "moderate":
            risk_score += 2
        elif risk_level == "mild":
            risk_score += 1
        elif risk_level == "beneficial":
            risk_score -= 1
    
    # Interaction multiplier
    risk_score += len(interactions) * 2
    
    if risk_score >= 6:
        overall_risk = "high"
    elif risk_score >= 3:
        overall_risk = "moderate"
    elif risk_score >= 1:
        overall_risk = "mild"
    else:
        overall_risk = "low"
    
    return {
        "drugs_analyzed": [d["drug_name"] for d in found_drugs],
        "drugs_not_found": not_found,
        "bacteria_decreased": list(all_bacteria_decreased.values()),
        "bacteria_increased": list(all_bacteria_increased.values()),
        "mental_health_impact": {
            "overall_risk": overall_risk,
            "concerns": mental_health_concerns
        },
        "physical_health_impact": physical_health_concerns,
        "drug_interactions": interactions,
        "recommendations": all_recommendations,
        "drug_details": found_drugs
    }

@app.post("/api/recommendations")
async def get_ai_recommendations(request: AnalyzeRequest):
    """Get AI-powered personalized recommendations."""
    if not ANTHROPIC_API_KEY:
        raise HTTPException(status_code=503, detail="AI recommendations unavailable (no API key)")
    
    # First get the analysis
    analysis = await analyze_drugs(request)
    
    # Build prompt
    prompt = f"""You are a pharmacist and gut health expert. A user is taking these medications:
{', '.join(analysis['drugs_analyzed'])}

Based on research, here's what we know about their microbiome effects:

BACTERIA DECREASED:
{json.dumps(analysis['bacteria_decreased'], indent=2)}

BACTERIA INCREASED:
{json.dumps(analysis['bacteria_increased'], indent=2)}

DRUG INTERACTIONS:
{json.dumps(analysis['drug_interactions'], indent=2)}

Please provide personalized recommendations in this JSON format:
{{
    "summary": "2-3 sentence summary of the overall microbiome impact",
    "top_concerns": ["concern 1", "concern 2", "concern 3"],
    "probiotic_suggestions": [
        {{"strain": "Lactobacillus rhamnosus", "reason": "why this helps"}}
    ],
    "dietary_suggestions": [
        {{"food": "food name", "benefit": "how it helps"}}
    ],
    "timing_suggestions": ["when to take meds relative to each other"],
    "lifestyle_suggestions": ["other helpful tips"],
    "when_to_consult_doctor": ["red flags to watch for"]
}}

Respond ONLY with valid JSON, no markdown."""

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": ANTHROPIC_API_KEY,
                    "anthropic-version": "2023-06-01"
                },
                json={
                    "model": "claude-sonnet-4-20250514",
                    "max_tokens": 1500,
                    "messages": [{"role": "user", "content": prompt}]
                },
                timeout=60
            )
            response.raise_for_status()
        
        data = response.json()
        text = data.get("content", [{}])[0].get("text", "")
        
        # Parse JSON
        json_match = re.search(r'\{[\s\S]*\}', text)
        if json_match:
            ai_recommendations = json.loads(json_match.group(0))
            return {
                **analysis,
                "ai_recommendations": ai_recommendations
            }
        else:
            return analysis
            
    except Exception as e:
        logger.error(f"AI recommendation error: {e}")
        return analysis

# =============================================================================
# Run
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
