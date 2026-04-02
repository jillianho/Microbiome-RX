"""
MicrobiomeRx - Drug-Microbiome Interaction Database

This module contains research-backed data on how common medications
affect the gut microbiome and subsequent health impacts.

KEY REFERENCES:
1. Maier L, et al. (2018) "Extensive impact of non-antibiotic drugs on human gut bacteria."
   Nature 555:623-628. doi:10.1038/nature25979
   - Screened 1,000+ drugs against 40 gut bacteria strains
   - Found 24% of non-antibiotics inhibit gut bacteria

2. Imhann F, et al. (2016) "Proton pump inhibitors affect the gut microbiome."
   Gut 65:740-748. doi:10.1136/gutjnl-2015-310376
   - PPIs associated with decreased bacterial diversity
   - Increased Enterococcus, Streptococcus

3. Vich Vila A, et al. (2020) "Impact of commonly used drugs on the composition and 
   metabolic function of the gut microbiota." Nature Communications 11:362.
   - Analyzed 41 drug categories in 1,883 individuals
   - Identified specific bacterial changes per drug class

4. Flowers SA, et al. (2019) "The microbiome in mental health: Potential contribution 
   of gut microbiota in disease and pharmacotherapy." Pharmacotherapy 39(7):751-762.
   - Review of psychotropic drug-microbiome interactions

5. Rogers MAM, Aronoff DM. (2016) "The influence of non-steroidal anti-inflammatory drugs 
   on the gut microbiome." Clinical Microbiology and Infection 22:178.e1-178.e9.
   - NSAIDs alter microbiome composition
   - Contribute to gut permeability

6. Duan X, et al. (2024) "Semaglutide alleviates gut microbiota dysbiosis induced by 
   a high-fat diet." European Journal of Pharmacology 969:176440.
   - Semaglutide significantly increased Akkermansia abundance
   - Restored gut barrier tight junction proteins

7. Feng J, et al. (2024) "Effects of semaglutide on gut microbiota, cognitive function 
   and inflammation in obese mice." PeerJ 12:e17891.
   - Semaglutide reversed HFD-induced gut microbiota dysbiosis
   - Akkermansia increased ~166x vs HFD group

8. Gofron KK, et al. (2025) "Effects of GLP-1 analogues and agonists on the gut 
   microbiota: a systematic review." Nutrients 17(8):1303.
   - Systematic review of 38 studies on GLP-1 drugs and microbiome
   - A. muciniphila consistently increased across GLP-1 agonists

9. Hammouda ZK, et al. (2025) "Fexofenadine HCl enhances growth, biofilm, and lactic 
   acid production of Limosilactobacillus reuteri and Bifidobacterium longum." 
   BMC Microbiology.
   - Fexofenadine enhanced beneficial bacteria growth
   - Cetirizine and desloratadine inhibited tested bacteria

10. Xie Y, et al. (2024) "Loratadine as an anti-inflammatory agent against 
    Clostridium difficile toxin B." J Infectious Diseases 230(3):545.
    - Loratadine showed anti-inflammatory effects against C. diff toxin

NOTE: This is for educational/demonstration purposes only.
Not intended for clinical decision-making.
"""

from typing import Dict, List, Any

# =============================================================================
# DRUG-MICROBIOME INTERACTION DATABASE
# =============================================================================

DRUG_DATABASE: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # PROTON PUMP INHIBITORS (PPIs)
    # =========================================================================
    "omeprazole": {
        "drug_name": "Omeprazole",
        "brand_names": ["Prilosec", "Losec"],
        "drug_class": "Proton Pump Inhibitor",
        "common_uses": ["GERD", "Acid reflux", "Ulcers"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "moderate", "mechanism": "Altered stomach pH allows pathogen overgrowth"},
                {"bacteria": "Bifidobacterium", "magnitude": "mild", "mechanism": "pH-dependent growth inhibition"},
                {"bacteria": "Faecalibacterium", "magnitude": "mild", "mechanism": "Indirect effect via ecosystem shift"},
            ],
            "increases": [
                {"bacteria": "Enterococcus", "magnitude": "significant", "mechanism": "Thrives in higher pH environment"},
                {"bacteria": "Streptococcus", "magnitude": "moderate", "mechanism": "Oral bacteria survive to gut"},
                {"bacteria": "Enterobacteriaceae", "magnitude": "moderate", "mechanism": "Reduced acid barrier"},
            ],
            "overall_diversity": "decreased",
            "evidence_strength": "strong"
        },
        "mental_health_impact": {
            "risk_level": "moderate",
            "effects": [
                "Reduced Lactobacillus may decrease GABA production",
                "Increased Enterobacteriaceae linked to inflammation and depression",
                "Long-term use associated with B12 deficiency → mood effects"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "Increased risk of C. difficile infection", "severity": "moderate"},
                {"system": "Immune", "impact": "Reduced colonization resistance", "severity": "mild"},
                {"system": "Metabolic", "impact": "B12 and magnesium malabsorption", "severity": "moderate"},
            ]
        },
        "recommendations": [
            "Consider probiotic with Lactobacillus strains",
            "Monitor B12 levels with long-term use",
            "Take at lowest effective dose",
            "Consider periodic drug holidays if appropriate"
        ],
        "citations": ["Imhann 2016", "Maier 2018"]
    },
    
    "esomeprazole": {
        "drug_name": "Esomeprazole",
        "brand_names": ["Nexium"],
        "drug_class": "Proton Pump Inhibitor",
        "common_uses": ["GERD", "Acid reflux", "Ulcers"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "moderate", "mechanism": "Altered stomach pH"},
                {"bacteria": "Bifidobacterium", "magnitude": "mild", "mechanism": "pH-dependent effects"},
            ],
            "increases": [
                {"bacteria": "Enterococcus", "magnitude": "significant", "mechanism": "Higher pH environment"},
                {"bacteria": "Streptococcus", "magnitude": "moderate", "mechanism": "Oral-gut translocation"},
            ],
            "overall_diversity": "decreased",
            "evidence_strength": "strong"
        },
        "mental_health_impact": {
            "risk_level": "moderate",
            "effects": [
                "Similar to omeprazole — reduced beneficial bacteria",
                "Potential indirect effects via nutrient malabsorption"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "C. difficile risk", "severity": "moderate"},
                {"system": "Bone", "impact": "Long-term fracture risk", "severity": "mild"},
            ]
        },
        "recommendations": [
            "Consider probiotic supplementation",
            "Periodic reassessment of need",
            "Calcium and B12 monitoring"
        ],
        "citations": ["Imhann 2016"]
    },

    # =========================================================================
    # SELECTIVE SEROTONIN REUPTAKE INHIBITORS (SSRIs)
    # =========================================================================
    "sertraline": {
        "drug_name": "Sertraline",
        "brand_names": ["Zoloft"],
        "drug_class": "SSRI Antidepressant",
        "common_uses": ["Depression", "Anxiety", "OCD", "PTSD"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "mild", "mechanism": "Direct antimicrobial activity"},
                {"bacteria": "Clostridium", "magnitude": "mild", "mechanism": "Growth inhibition"},
            ],
            "increases": [
                {"bacteria": "Bacteroides", "magnitude": "mild", "mechanism": "Indirect selection"},
            ],
            "overall_diversity": "mildly decreased",
            "evidence_strength": "moderate"
        },
        "mental_health_impact": {
            "risk_level": "low",
            "effects": [
                "Primary effect is therapeutic (treats depression/anxiety)",
                "Microbiome changes may contribute to GI side effects",
                "Some evidence gut changes contribute to efficacy"
            ],
            "evidence_strength": "emerging"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "Nausea, diarrhea common initially", "severity": "mild"},
                {"system": "Metabolic", "impact": "Weight changes possible", "severity": "mild"},
            ]
        },
        "recommendations": [
            "Probiotic may help with GI side effects",
            "Fiber intake supports beneficial bacteria",
            "GI symptoms often improve after 2-4 weeks"
        ],
        "citations": ["Maier 2018", "Flowers 2019"]
    },
    
    "escitalopram": {
        "drug_name": "Escitalopram",
        "brand_names": ["Lexapro", "Cipralex"],
        "drug_class": "SSRI Antidepressant",
        "common_uses": ["Depression", "Generalized anxiety"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "mild", "mechanism": "Antimicrobial properties"},
            ],
            "increases": [],
            "overall_diversity": "minimal change",
            "evidence_strength": "emerging"
        },
        "mental_health_impact": {
            "risk_level": "low",
            "effects": [
                "Therapeutic benefit for depression/anxiety",
                "Minimal negative microbiome impact compared to other drugs",
                "May actually improve gut-brain signaling"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "Initial nausea possible", "severity": "mild"},
            ]
        },
        "recommendations": [
            "Generally well-tolerated regarding gut health",
            "Probiotic may support overall wellbeing",
            "Maintain fiber-rich diet"
        ],
        "citations": ["Flowers 2019"]
    },
    
    "fluoxetine": {
        "drug_name": "Fluoxetine",
        "brand_names": ["Prozac"],
        "drug_class": "SSRI Antidepressant",
        "common_uses": ["Depression", "OCD", "Bulimia", "Panic disorder"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "moderate", "mechanism": "Direct antimicrobial effect"},
                {"bacteria": "Clostridium", "magnitude": "mild", "mechanism": "Growth inhibition"},
            ],
            "increases": [
                {"bacteria": "Prevotella", "magnitude": "mild", "mechanism": "Indirect selection"},
            ],
            "overall_diversity": "mildly decreased",
            "evidence_strength": "moderate"
        },
        "mental_health_impact": {
            "risk_level": "low",
            "effects": [
                "Primary therapeutic effect on depression",
                "Antimicrobial activity may contribute to mechanism",
                "Long half-life means stable gut exposure"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "Appetite changes common", "severity": "mild"},
                {"system": "Metabolic", "impact": "Weight loss initially common", "severity": "mild"},
            ]
        },
        "recommendations": [
            "Probiotic with Lactobacillus strains may help",
            "Stay hydrated",
            "Fiber supports microbiome resilience"
        ],
        "citations": ["Maier 2018", "Flowers 2019"]
    },

    # =========================================================================
    # NSAIDs
    # =========================================================================
    "ibuprofen": {
        "drug_name": "Ibuprofen",
        "brand_names": ["Advil", "Motrin", "Nurofen"],
        "drug_class": "NSAID",
        "common_uses": ["Pain", "Inflammation", "Fever", "Arthritis"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Akkermansia", "magnitude": "moderate", "mechanism": "Mucus layer damage"},
                {"bacteria": "Faecalibacterium", "magnitude": "mild", "mechanism": "Gut barrier disruption"},
                {"bacteria": "Roseburia", "magnitude": "mild", "mechanism": "Inflammation effects"},
            ],
            "increases": [
                {"bacteria": "Enterobacteriaceae", "magnitude": "moderate", "mechanism": "Gut permeability allows overgrowth"},
                {"bacteria": "Erysipelotrichaceae", "magnitude": "mild", "mechanism": "Inflammatory environment"},
            ],
            "overall_diversity": "decreased with chronic use",
            "evidence_strength": "moderate"
        },
        "mental_health_impact": {
            "risk_level": "moderate",
            "effects": [
                "Gut barrier damage increases systemic inflammation",
                "Inflammation linked to depression risk",
                "Reduced butyrate production affects brain signaling"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "GI bleeding risk, ulcers", "severity": "significant"},
                {"system": "Gut barrier", "impact": "Increased permeability (leaky gut)", "severity": "moderate"},
                {"system": "Cardiovascular", "impact": "Increased CV risk with chronic use", "severity": "moderate"},
            ]
        },
        "recommendations": [
            "Take with food to reduce GI impact",
            "Use lowest effective dose for shortest duration",
            "Consider Akkermansia-supporting foods (polyphenols)",
            "Probiotic may help maintain barrier function"
        ],
        "citations": ["Rogers 2016", "Vich Vila 2020"]
    },
    
    "naproxen": {
        "drug_name": "Naproxen",
        "brand_names": ["Aleve", "Naprosyn"],
        "drug_class": "NSAID",
        "common_uses": ["Pain", "Inflammation", "Arthritis"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Akkermansia", "magnitude": "moderate", "mechanism": "Mucus layer effects"},
                {"bacteria": "Faecalibacterium", "magnitude": "mild", "mechanism": "Barrier disruption"},
            ],
            "increases": [
                {"bacteria": "Enterobacteriaceae", "magnitude": "moderate", "mechanism": "Permeability changes"},
            ],
            "overall_diversity": "decreased with chronic use",
            "evidence_strength": "moderate"
        },
        "mental_health_impact": {
            "risk_level": "moderate",
            "effects": [
                "Similar to ibuprofen — inflammation pathway",
                "Longer half-life means prolonged gut exposure"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "GI bleeding risk", "severity": "significant"},
                {"system": "Renal", "impact": "Kidney function effects", "severity": "moderate"},
            ]
        },
        "recommendations": [
            "Take with food",
            "Limit duration of use",
            "Consider gut-protective strategies"
        ],
        "citations": ["Rogers 2016"]
    },
    
    "aspirin": {
        "drug_name": "Aspirin",
        "brand_names": ["Bayer", "Bufferin"],
        "drug_class": "NSAID / Antiplatelet",
        "common_uses": ["Pain", "Heart disease prevention", "Inflammation"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Akkermansia", "magnitude": "mild", "mechanism": "Mucus effects"},
                {"bacteria": "Prevotella", "magnitude": "mild", "mechanism": "Direct inhibition"},
            ],
            "increases": [
                {"bacteria": "Bacteroides", "magnitude": "mild", "mechanism": "Selection effects"},
            ],
            "overall_diversity": "minimal change at low doses",
            "evidence_strength": "moderate"
        },
        "mental_health_impact": {
            "risk_level": "low",
            "effects": [
                "Low-dose aspirin has minimal microbiome impact",
                "Anti-inflammatory effects may be neuroprotective",
                "High doses have NSAID-like effects"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "GI bleeding risk (dose-dependent)", "severity": "mild to moderate"},
                {"system": "Cardiovascular", "impact": "Protective at low doses", "severity": "beneficial"},
            ]
        },
        "recommendations": [
            "Low-dose (81mg) has minimal gut impact",
            "Enteric coating may reduce GI effects",
            "Take with food if GI sensitive"
        ],
        "citations": ["Rogers 2016", "Vich Vila 2020"]
    },

    # =========================================================================
    # ANTIBIOTICS
    # =========================================================================
    "amoxicillin": {
        "drug_name": "Amoxicillin",
        "brand_names": ["Amoxil", "Moxatag"],
        "drug_class": "Penicillin Antibiotic",
        "common_uses": ["Bacterial infections", "Strep throat", "Ear infections"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "significant", "mechanism": "Direct killing"},
                {"bacteria": "Bifidobacterium", "magnitude": "significant", "mechanism": "Broad spectrum activity"},
                {"bacteria": "Faecalibacterium", "magnitude": "moderate", "mechanism": "Collateral damage"},
                {"bacteria": "Roseburia", "magnitude": "moderate", "mechanism": "Gram-positive targeting"},
            ],
            "increases": [
                {"bacteria": "Enterobacteriaceae", "magnitude": "significant", "mechanism": "Resistance/niche opening"},
                {"bacteria": "Clostridium difficile", "magnitude": "moderate", "mechanism": "Loss of colonization resistance"},
            ],
            "overall_diversity": "significantly decreased",
            "evidence_strength": "strong"
        },
        "mental_health_impact": {
            "risk_level": "high",
            "effects": [
                "Major disruption to GABA-producing Lactobacillus",
                "Loss of anti-inflammatory Faecalibacterium",
                "Recovery can take weeks to months",
                "Increased anxiety/depression reported during use"
            ],
            "evidence_strength": "strong"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "Diarrhea, nausea common", "severity": "moderate"},
                {"system": "Immune", "impact": "Reduced colonization resistance", "severity": "significant"},
                {"system": "Metabolic", "impact": "Vitamin K synthesis affected", "severity": "mild"},
            ]
        },
        "recommendations": [
            "Take probiotic 2+ hours apart from antibiotic",
            "Saccharomyces boulardii may prevent diarrhea",
            "Continue probiotic 2 weeks after course ends",
            "Eat fermented foods during recovery"
        ],
        "citations": ["Maier 2018"]
    },
    
    "azithromycin": {
        "drug_name": "Azithromycin",
        "brand_names": ["Zithromax", "Z-Pack"],
        "drug_class": "Macrolide Antibiotic",
        "common_uses": ["Respiratory infections", "Skin infections", "STIs"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "moderate", "mechanism": "Protein synthesis inhibition"},
                {"bacteria": "Bifidobacterium", "magnitude": "moderate", "mechanism": "Broad activity"},
                {"bacteria": "Actinobacteria", "magnitude": "significant", "mechanism": "Primary target"},
            ],
            "increases": [
                {"bacteria": "Proteobacteria", "magnitude": "moderate", "mechanism": "Resistance"},
            ],
            "overall_diversity": "moderately decreased",
            "evidence_strength": "strong"
        },
        "mental_health_impact": {
            "risk_level": "moderate",
            "effects": [
                "Disrupts beneficial bacteria populations",
                "Short course (3-5 days) limits damage",
                "Effects persist 1-2 weeks post-treatment"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "GI upset, diarrhea", "severity": "moderate"},
                {"system": "Cardiac", "impact": "QT prolongation risk", "severity": "rare but serious"},
            ]
        },
        "recommendations": [
            "Probiotic during and after treatment",
            "Short course minimizes microbiome damage",
            "Fiber supports recovery"
        ],
        "citations": ["Maier 2018"]
    },
    
    "ciprofloxacin": {
        "drug_name": "Ciprofloxacin",
        "brand_names": ["Cipro"],
        "drug_class": "Fluoroquinolone Antibiotic",
        "common_uses": ["UTIs", "Respiratory infections", "GI infections"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "significant", "mechanism": "Broad spectrum killing"},
                {"bacteria": "Bifidobacterium", "magnitude": "significant", "mechanism": "DNA gyrase inhibition"},
                {"bacteria": "Faecalibacterium", "magnitude": "significant", "mechanism": "Major disruption"},
                {"bacteria": "Roseburia", "magnitude": "moderate", "mechanism": "Collateral damage"},
                {"bacteria": "Coprococcus", "magnitude": "moderate", "mechanism": "Broad effects"},
            ],
            "increases": [
                {"bacteria": "Enterococcus", "magnitude": "significant", "mechanism": "Intrinsic resistance"},
                {"bacteria": "Candida", "magnitude": "moderate", "mechanism": "Fungal overgrowth"},
            ],
            "overall_diversity": "severely decreased",
            "evidence_strength": "strong"
        },
        "mental_health_impact": {
            "risk_level": "high",
            "effects": [
                "Severe microbiome disruption",
                "CNS effects reported (anxiety, depression, psychosis)",
                "Recovery may take months",
                "Loss of multiple protective species"
            ],
            "evidence_strength": "strong"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "Severe diarrhea, C. diff risk", "severity": "significant"},
                {"system": "Musculoskeletal", "impact": "Tendon damage risk", "severity": "moderate"},
                {"system": "Nervous", "impact": "Neuropathy risk", "severity": "moderate"},
            ]
        },
        "recommendations": [
            "Reserve for serious infections only",
            "High-dose multi-strain probiotic essential",
            "S. boulardii for C. diff prevention",
            "Prolonged recovery protocol (4+ weeks probiotic)"
        ],
        "citations": ["Maier 2018"]
    },

    # =========================================================================
    # METFORMIN
    # =========================================================================
    "metformin": {
        "drug_name": "Metformin",
        "brand_names": ["Glucophage", "Fortamet"],
        "drug_class": "Biguanide Antidiabetic",
        "common_uses": ["Type 2 diabetes", "PCOS", "Prediabetes"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Intestinibacter", "magnitude": "moderate", "mechanism": "Direct inhibition"},
            ],
            "increases": [
                {"bacteria": "Akkermansia", "magnitude": "significant", "mechanism": "Mucin production enhancement"},
                {"bacteria": "Bifidobacterium", "magnitude": "moderate", "mechanism": "SCFA pathway"},
                {"bacteria": "Lactobacillus", "magnitude": "mild", "mechanism": "Indirect support"},
                {"bacteria": "Escherichia", "magnitude": "mild", "mechanism": "Glucose availability"},
            ],
            "overall_diversity": "increased (beneficial shift)",
            "evidence_strength": "strong"
        },
        "mental_health_impact": {
            "risk_level": "beneficial",
            "effects": [
                "Increases Akkermansia — anti-inflammatory",
                "Supports beneficial bacteria linked to mood",
                "May explain some metabolic-mood benefits",
                "Initial GI distress can cause temporary distress"
            ],
            "evidence_strength": "strong"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Metabolic", "impact": "Improves insulin sensitivity", "severity": "beneficial"},
                {"system": "Digestive", "impact": "Initial GI upset common", "severity": "mild, temporary"},
                {"system": "Gut barrier", "impact": "Improves barrier function via Akkermansia", "severity": "beneficial"},
            ]
        },
        "recommendations": [
            "Start low, increase slowly to reduce GI effects",
            "GI side effects often improve over time",
            "Extended-release formulation easier on gut",
            "One of few drugs with positive microbiome effects"
        ],
        "citations": ["Vich Vila 2020", "Maier 2018"]
    },

    # =========================================================================
    # GLP-1 RECEPTOR AGONISTS
    # =========================================================================
    "semaglutide": {
        "drug_name": "Semaglutide",
        "brand_names": ["Ozempic", "Wegovy", "Rybelsus"],
        "drug_class": "GLP-1 Receptor Agonist",
        "common_uses": ["Type 2 diabetes", "Obesity", "Weight management"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Desulfovibrionaceae", "magnitude": "moderate", "mechanism": "Reduced abundance of sulfate-reducing bacteria linked to inflammation"},
                {"bacteria": "Romboutsia", "magnitude": "moderate", "mechanism": "Shifts away from obesity-associated taxa"},
                {"bacteria": "Lachnospiraceae_NK4A136_group", "magnitude": "moderate", "mechanism": "Compositional shift toward healthier profile"},
            ],
            "increases": [
                {"bacteria": "Akkermansia", "magnitude": "significant", "mechanism": "Enhanced mucin production and gut barrier integrity"},
                {"bacteria": "Muribaculaceae", "magnitude": "moderate", "mechanism": "Supports SCFA production (succinate, acetate, propionate)"},
                {"bacteria": "Allobaculum", "magnitude": "moderate", "mechanism": "Restored by semaglutide in dysbiotic states"},
                {"bacteria": "Lactobacillus", "magnitude": "mild", "mechanism": "Indirect support via improved gut environment"},
            ],
            "overall_diversity": "restored toward healthy baseline (variable across studies)",
            "evidence_strength": "emerging"
        },
        "mental_health_impact": {
            "risk_level": "beneficial",
            "effects": [
                "Increased Akkermansia linked to reduced neuroinflammation",
                "Attenuates anxiety and depressive-like behaviors via microbiota-gut-brain axis",
                "Reduces pro-inflammatory cytokines IL-6 and IL-1β",
                "Improved cognitive function observed in obese mouse models",
                "Initial GI symptoms (nausea) may cause temporary distress"
            ],
            "evidence_strength": "moderate (animal studies; human microbiome data emerging)"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Metabolic", "impact": "Significant weight loss and improved insulin sensitivity", "severity": "beneficial"},
                {"system": "Gut barrier", "impact": "Restores tight junction proteins (occludin, Tjp1) and Muc-2 expression", "severity": "beneficial"},
                {"system": "Digestive", "impact": "Nausea, vomiting, diarrhea common initially", "severity": "mild to moderate, temporary"},
                {"system": "Inflammatory", "impact": "Reduced systemic and hepatic inflammation", "severity": "beneficial"},
            ]
        },
        "recommendations": [
            "Start at low dose and titrate up to reduce GI side effects",
            "GI side effects (nausea) typically improve over weeks",
            "One of few drugs with positive microbiome effects (similar to metformin)",
            "May synergize with Akkermansia-supporting foods (polyphenols, fiber)",
            "Monitor for pancreatitis symptoms (rare but serious)"
        ],
        "citations": ["Duan 2024", "Feng 2024", "Gofron 2025", "de Paiva 2024", "Chen 2025"]
    },

    # =========================================================================
    # STATINS
    # =========================================================================
    "atorvastatin": {
        "drug_name": "Atorvastatin",
        "brand_names": ["Lipitor"],
        "drug_class": "Statin",
        "common_uses": ["High cholesterol", "Cardiovascular disease prevention"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Clostridium", "magnitude": "mild", "mechanism": "Bile acid changes"},
            ],
            "increases": [
                {"bacteria": "Bacteroides", "magnitude": "mild", "mechanism": "Bile acid metabolism"},
                {"bacteria": "Lactobacillus", "magnitude": "mild", "mechanism": "Indirect effects"},
            ],
            "overall_diversity": "minimal change to slight increase",
            "evidence_strength": "emerging"
        },
        "mental_health_impact": {
            "risk_level": "low",
            "effects": [
                "Minimal direct microbiome effects",
                "Some reports of mood effects (mechanism unclear)",
                "Anti-inflammatory effects may be beneficial"
            ],
            "evidence_strength": "limited"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Cardiovascular", "impact": "Reduces cholesterol, CV risk", "severity": "beneficial"},
                {"system": "Muscular", "impact": "Myopathy risk in some", "severity": "mild to moderate"},
            ]
        },
        "recommendations": [
            "Generally microbiome-neutral",
            "CoQ10 supplement may help muscle symptoms",
            "No specific probiotic needed for this drug"
        ],
        "citations": ["Vich Vila 2020"]
    },

    # =========================================================================
    # ORAL CONTRACEPTIVES
    # =========================================================================
    "ethinyl_estradiol_levonorgestrel": {
        "drug_name": "Combined Oral Contraceptive",
        "brand_names": ["Various birth control pills"],
        "drug_class": "Hormonal Contraceptive",
        "common_uses": ["Contraception", "Menstrual regulation", "Acne"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus (gut)", "magnitude": "mild", "mechanism": "Hormone-microbiome interaction"},
            ],
            "increases": [
                {"bacteria": "Bacteroides", "magnitude": "mild", "mechanism": "Estrogen metabolism"},
                {"bacteria": "Prevotella", "magnitude": "mild", "mechanism": "Hormone effects"},
            ],
            "overall_diversity": "mild changes",
            "evidence_strength": "emerging"
        },
        "mental_health_impact": {
            "risk_level": "mild",
            "effects": [
                "Mood changes reported in some users",
                "Microbiome shifts may contribute",
                "Estrogen affects gut-brain axis",
                "Individual variation is high"
            ],
            "evidence_strength": "emerging"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Reproductive", "impact": "Contraceptive efficacy", "severity": "beneficial"},
                {"system": "Digestive", "impact": "Mild GI changes in some", "severity": "mild"},
            ]
        },
        "recommendations": [
            "Probiotic may help if GI symptoms present",
            "Monitor mood changes",
            "Maintain diverse diet for microbiome health"
        ],
        "citations": ["Vich Vila 2020"]
    },

    # =========================================================================
    # SECOND-GENERATION ANTIHISTAMINES
    # =========================================================================
    "cetirizine": {
        "drug_name": "Cetirizine",
        "brand_names": ["Zyrtec", "Reactine"],
        "drug_class": "Second-Generation Antihistamine",
        "common_uses": ["Allergic rhinitis", "Urticaria", "Hay fever", "Allergies"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "mild", "mechanism": "In vitro growth inhibition of beneficial strains"},
                {"bacteria": "Bifidobacterium", "magnitude": "mild", "mechanism": "Direct antimicrobial activity at gut concentrations"},
            ],
            "increases": [],
            "overall_diversity": "minimal change at standard doses",
            "evidence_strength": "emerging"
        },
        "mental_health_impact": {
            "risk_level": "low",
            "effects": [
                "Minimal CNS penetration (second-generation)",
                "Mild sedation possible — less than first-generation antihistamines",
                "Mildly inhibits beneficial bacteria (unlike fexofenadine, which promotes them)",
                "No significant mood effects reported"
            ],
            "evidence_strength": "limited"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Immune", "impact": "Effective allergy symptom relief", "severity": "beneficial"},
                {"system": "Digestive", "impact": "Mild inhibition of Lactobacillus and Bifidobacterium; consider fexofenadine for better gut profile", "severity": "mild"},
                {"system": "CNS", "impact": "Mild drowsiness in some individuals", "severity": "mild"},
            ]
        },
        "recommendations": [
            "Has the most antimicrobial activity of the three common second-gen antihistamines",
            "Mildly inhibits Lactobacillus and Bifidobacterium in vitro — clinical significance at standard doses unclear",
            "If gut health is a priority, switch to fexofenadine (Allegra), which uniquely promotes beneficial bacteria",
            "Probiotic support may help offset mild inhibitory effects during long-term use"
        ],
        "citations": ["Maier 2018", "Hammouda 2025"]
    },

    "loratadine": {
        "drug_name": "Loratadine",
        "brand_names": ["Claritin", "Alavert"],
        "drug_class": "Second-Generation Antihistamine",
        "common_uses": ["Allergic rhinitis", "Urticaria", "Hay fever", "Allergies"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "mild", "mechanism": "Mild antimicrobial properties"},
            ],
            "increases": [],
            "overall_diversity": "minimal change",
            "evidence_strength": "emerging"
        },
        "mental_health_impact": {
            "risk_level": "low",
            "effects": [
                "Non-sedating — minimal CNS effects",
                "No significant microbiome-mediated mood effects reported",
                "Anti-inflammatory properties may have indirect benefits",
                "Milder antimicrobial effects than cetirizine; fexofenadine is the best gut option"
            ],
            "evidence_strength": "limited"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Immune", "impact": "Effective allergy symptom relief", "severity": "beneficial"},
                {"system": "Digestive", "impact": "Mild Lactobacillus inhibition; anti-inflammatory effect against C. difficile toxin B", "severity": "mild"},
            ]
        },
        "recommendations": [
            "Middle option for gut health — milder antimicrobial effects than cetirizine (Zyrtec)",
            "Bonus: shows anti-inflammatory properties against C. difficile toxin B",
            "For best microbiome outcome, fexofenadine (Allegra) is preferred — it actively promotes beneficial bacteria",
            "No specific probiotic intervention needed at standard doses"
        ],
        "citations": ["Maier 2018", "Xie 2024"]
    },

    "fexofenadine": {
        "drug_name": "Fexofenadine",
        "brand_names": ["Allegra", "Telfast"],
        "drug_class": "Second-Generation Antihistamine",
        "common_uses": ["Allergic rhinitis", "Urticaria", "Hay fever", "Allergies"],
        "microbiome_effects": {
            "decreases": [],
            "increases": [
                {"bacteria": "Lactobacillus reuteri", "magnitude": "mild", "mechanism": "Enhanced growth and biofilm formation of beneficial strains"},
                {"bacteria": "Bifidobacterium longum", "magnitude": "mild", "mechanism": "Enhanced growth and lactic acid production"},
            ],
            "overall_diversity": "minimal change to mildly beneficial",
            "evidence_strength": "emerging"
        },
        "mental_health_impact": {
            "risk_level": "low",
            "effects": [
                "Non-sedating — does not cross blood-brain barrier",
                "No significant CNS or mood effects",
                "Only antihistamine shown to promote beneficial gut bacteria (may support gut-brain axis)"
            ],
            "evidence_strength": "emerging"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Immune", "impact": "Effective allergy symptom relief", "severity": "beneficial"},
                {"system": "Digestive", "impact": "Promotes Lactobacillus and Bifidobacterium growth — opposite effect to cetirizine/loratadine", "severity": "beneficial"},
            ]
        },
        "recommendations": [
            "Best antihistamine for gut health — the only one shown to promote beneficial bacteria",
            "Enhances Lactobacillus reuteri and Bifidobacterium longum (cetirizine and loratadine mildly inhibit them)",
            "Recommended first-line antihistamine for patients concerned about microbiome",
            "Non-sedating (does not cross blood-brain barrier) and well-tolerated"
        ],
        "citations": ["Hammouda 2025", "Maier 2018"]
    },

    # =========================================================================
    # BENZODIAZEPINES
    # =========================================================================
    "alprazolam": {
        "drug_name": "Alprazolam",
        "brand_names": ["Xanax"],
        "drug_class": "Benzodiazepine",
        "common_uses": ["Anxiety", "Panic disorder"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "mild", "mechanism": "GABA pathway interaction"},
            ],
            "increases": [],
            "overall_diversity": "minimal change",
            "evidence_strength": "emerging"
        },
        "mental_health_impact": {
            "risk_level": "low (direct)",
            "effects": [
                "Therapeutic effect on anxiety",
                "Minimal direct microbiome impact",
                "Dependence risk is the main concern"
            ],
            "evidence_strength": "limited"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "CNS", "impact": "Sedation, dependence risk", "severity": "moderate"},
            ]
        },
        "recommendations": [
            "No specific microbiome interventions needed",
            "Focus on anxiety management strategies",
            "Work with doctor on appropriate use"
        ],
        "citations": ["Flowers 2019"]
    },

    # =========================================================================
    # OPIOIDS
    # =========================================================================
    "oxycodone": {
        "drug_name": "Oxycodone",
        "brand_names": ["OxyContin", "Percocet"],
        "drug_class": "Opioid Analgesic",
        "common_uses": ["Severe pain"],
        "microbiome_effects": {
            "decreases": [
                {"bacteria": "Lactobacillus", "magnitude": "moderate", "mechanism": "Gut motility effects"},
                {"bacteria": "Bifidobacterium", "magnitude": "moderate", "mechanism": "Transit time changes"},
                {"bacteria": "Faecalibacterium", "magnitude": "mild", "mechanism": "Environmental shift"},
            ],
            "increases": [
                {"bacteria": "Enterococcus", "magnitude": "moderate", "mechanism": "Constipation environment"},
                {"bacteria": "Staphylococcus", "magnitude": "mild", "mechanism": "Immune suppression"},
            ],
            "overall_diversity": "decreased",
            "evidence_strength": "moderate"
        },
        "mental_health_impact": {
            "risk_level": "moderate",
            "effects": [
                "Constipation disrupts gut-brain axis",
                "Dependence affects mental health",
                "Opioid-induced hyperalgesia",
                "Withdrawal has gut components"
            ],
            "evidence_strength": "moderate"
        },
        "physical_health_impact": {
            "effects": [
                {"system": "Digestive", "impact": "Severe constipation", "severity": "significant"},
                {"system": "Immune", "impact": "Immunosuppression", "severity": "moderate"},
                {"system": "Respiratory", "impact": "Depression risk", "severity": "serious"},
            ]
        },
        "recommendations": [
            "Fiber and hydration for constipation",
            "Probiotic to maintain diversity",
            "Work with pain specialist",
            "Consider non-opioid alternatives when possible"
        ],
        "citations": ["Vich Vila 2020"]
    },
}

# =============================================================================
# DRUG CLASS SUMMARIES
# =============================================================================

DRUG_CLASS_EFFECTS = {
    "Proton Pump Inhibitor": {
        "overall_impact": "negative",
        "summary": "PPIs reduce stomach acid, allowing oral bacteria to survive into the gut and disrupting the normal microbiome balance. Associated with decreased diversity and increased infection risk.",
        "key_concerns": ["C. difficile risk", "Reduced beneficial bacteria", "B12 malabsorption"],
    },
    "SSRI Antidepressant": {
        "overall_impact": "mixed",
        "summary": "SSRIs have direct antimicrobial activity against some gut bacteria. Effects are generally mild, and therapeutic benefits typically outweigh microbiome concerns.",
        "key_concerns": ["Initial GI symptoms", "Mild Lactobacillus reduction"],
    },
    "NSAID": {
        "overall_impact": "negative",
        "summary": "NSAIDs damage the gut lining, reduce mucus-protecting Akkermansia, and increase gut permeability. Chronic use has significant microbiome impact.",
        "key_concerns": ["Gut barrier damage", "Increased inflammation", "GI bleeding"],
    },
    "Penicillin Antibiotic": {
        "overall_impact": "very negative",
        "summary": "Broad-spectrum antibiotics cause major disruption to gut bacteria, killing beneficial species along with pathogens. Recovery can take weeks to months.",
        "key_concerns": ["Severe dysbiosis", "C. difficile risk", "Long recovery"],
    },
    "Fluoroquinolone Antibiotic": {
        "overall_impact": "severely negative",
        "summary": "Fluoroquinolones cause severe, long-lasting microbiome damage. Should be reserved for serious infections due to both microbiome and other adverse effects.",
        "key_concerns": ["Severe dysbiosis", "CNS effects", "Tendon damage", "Prolonged recovery"],
    },
    "Biguanide Antidiabetic": {
        "overall_impact": "positive",
        "summary": "Metformin is one of the few drugs that improves the gut microbiome, increasing beneficial Akkermansia and supporting metabolic health through the gut.",
        "key_concerns": ["Initial GI upset (usually temporary)"],
    },
    "Statin": {
        "overall_impact": "neutral",
        "summary": "Statins have minimal direct effects on the gut microbiome. They work through lipid metabolism rather than gut bacteria.",
        "key_concerns": ["Minimal microbiome concerns"],
    },
    "Opioid Analgesic": {
        "overall_impact": "negative",
        "summary": "Opioids slow gut motility, causing constipation that disrupts the microbiome. They also affect immune function, which impacts gut bacteria.",
        "key_concerns": ["Severe constipation", "Dysbiosis", "Immune effects"],
    },
    "GLP-1 Receptor Agonist": {
        "overall_impact": "positive",
        "summary": "GLP-1 receptor agonists like semaglutide have been shown to significantly increase beneficial Akkermansia, restore gut barrier integrity, and shift microbiota composition toward a healthier profile. Effects are similar to metformin in being one of the few drug classes that improve the gut microbiome.",
        "key_concerns": ["Initial GI side effects (nausea, vomiting)", "Effects may vary by metabolic state"],
    },
    "Second-Generation Antihistamine": {
        "overall_impact": "varies by drug",
        "summary": "Not all antihistamines are equal for gut health. Fexofenadine (Allegra) is the clear winner — it uniquely promotes Lactobacillus and Bifidobacterium growth. Loratadine (Claritin) is a neutral middle ground with a C. diff–protective bonus. Cetirizine (Zyrtec) has the most antimicrobial activity, mildly inhibiting beneficial bacteria. For allergy patients who care about their microbiome, fexofenadine is the best choice.",
        "key_concerns": ["Cetirizine mildly inhibits Lactobacillus & Bifidobacterium", "Fexofenadine is the gut-friendly choice"],
    },
}

# =============================================================================
# INTERACTION RULES
# =============================================================================

DRUG_INTERACTIONS = {
    ("ppi", "nsaid"): {
        "severity": "moderate",
        "description": "Combined gut damage: PPIs reduce protective acid while NSAIDs damage gut lining. Increased risk of GI bleeding despite PPI.",
        "recommendation": "If both needed, use lowest doses and consider additional gut protection (probiotic, sucralfate)."
    },
    ("ppi", "antibiotic"): {
        "severity": "high",
        "description": "PPIs increase C. difficile risk, antibiotics cause dysbiosis. Combined risk is multiplicative.",
        "recommendation": "High-dose probiotic essential. Consider S. boulardii specifically for C. diff prevention."
    },
    ("nsaid", "ssri"): {
        "severity": "moderate",
        "description": "Both can affect GI tract. SSRIs increase bleeding risk which compounds with NSAID GI effects.",
        "recommendation": "Monitor for GI symptoms. Consider GI-protective strategies."
    },
    ("antibiotic", "antibiotic"): {
        "severity": "severe",
        "description": "Multiple antibiotics cause cumulative microbiome destruction. Recovery significantly prolonged.",
        "recommendation": "Intensive probiotic protocol. Extended recovery period (6+ weeks). Consider microbiome testing."
    },
    ("opioid", "ppi"): {
        "severity": "moderate",
        "description": "Opioid constipation plus PPI dysbiosis compounds gut dysfunction.",
        "recommendation": "Aggressive constipation management. Probiotic support."
    },
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def normalize_drug_name(name: str) -> str:
    """Normalize drug name for lookup."""
    return name.lower().strip().replace("-", "_").replace(" ", "_")

def find_drug(query: str) -> Dict | None:
    """Find drug by name or brand name."""
    query_normalized = normalize_drug_name(query)
    
    # Direct match
    if query_normalized in DRUG_DATABASE:
        return DRUG_DATABASE[query_normalized]
    
    # Search brand names
    for drug_key, drug_info in DRUG_DATABASE.items():
        for brand in drug_info.get("brand_names", []):
            if normalize_drug_name(brand) == query_normalized:
                return drug_info
    
    # Partial match
    for drug_key, drug_info in DRUG_DATABASE.items():
        if query_normalized in drug_key or drug_key in query_normalized:
            return drug_info
        for brand in drug_info.get("brand_names", []):
            brand_normalized = normalize_drug_name(brand)
            if query_normalized in brand_normalized or brand_normalized in query_normalized:
                return drug_info
    
    return None

def get_all_drug_names() -> List[str]:
    """Get list of all searchable drug names."""
    names = []
    for drug_key, drug_info in DRUG_DATABASE.items():
        names.append(drug_info["drug_name"])
        names.extend(drug_info.get("brand_names", []))
    return sorted(set(names))

def check_interactions(drugs: List[str]) -> List[Dict]:
    """Check for interactions between multiple drugs.
    
    Combines hardcoded clinical rules with dynamic detection of
    overlapping microbiome effects (compounding harm, opposing effects,
    and compounding beneficial bacteria increases).
    """
    interactions = []
    seen = set()  # deduplicate by drug pair + type
    
    # Resolve drug objects
    drug_objects = []
    for drug_name in drugs:
        drug = find_drug(drug_name)
        if drug:
            drug_objects.append(drug)
    
    # --- Phase 1: Hardcoded clinical interaction rules ---
    # Map drug classes to short keys used in DRUG_INTERACTIONS
    CLASS_KEY_MAP = {
        "proton pump inhibitor": "ppi",
        "ssri antidepressant": "ssri",
        "nsaid": "nsaid",
        "penicillin antibiotic": "antibiotic",
        "macrolide antibiotic": "antibiotic",
        "fluoroquinolone antibiotic": "antibiotic",
        "opioid analgesic": "opioid",
        "benzodiazepine": "benzodiazepine",
        "biguanide antidiabetic": "biguanide",
        "statin": "statin",
        "hormonal contraceptive": "contraceptive",
        "glp-1 receptor agonist": "glp1",
        "second-generation antihistamine": "antihistamine",
    }
    
    for i, d1 in enumerate(drug_objects):
        key1 = CLASS_KEY_MAP.get(d1["drug_class"].lower(), d1["drug_class"].lower().split()[0])
        for d2 in drug_objects[i+1:]:
            key2 = CLASS_KEY_MAP.get(d2["drug_class"].lower(), d2["drug_class"].lower().split()[0])
            for (c1, c2), interaction in DRUG_INTERACTIONS.items():
                if (c1 == key1 and c2 == key2) or (c2 == key1 and c1 == key2):
                    dup_key = (d1["drug_name"], d2["drug_name"], "clinical")
                    if dup_key not in seen:
                        seen.add(dup_key)
                        interactions.append({
                            "drugs": [d1["drug_name"], d2["drug_name"]],
                            "type": "clinical",
                            "confidence": "confirmed",
                            **interaction
                        })
    
    # --- Phase 2: Dynamic microbiome overlap detection ---
    MAGNITUDE_SCORE = {"mild": 1, "moderate": 2, "significant": 3}
    
    # Known harmful bacteria (increases are bad)
    HARMFUL_TAXA = {
        "enterococcus", "enterobacteriaceae", "clostridium difficile",
        "candida", "proteobacteria", "streptococcus",
        "erysipelotrichaceae", "desulfovibrionaceae",
    }
    
    # Known beneficial bacteria (decreases are bad)
    BENEFICIAL_TAXA = {
        "lactobacillus", "bifidobacterium", "akkermansia",
        "faecalibacterium", "roseburia", "coprococcus",
        "muribaculaceae", "allobaculum", "lactobacillus reuteri",
        "bifidobacterium longum",
    }
    
    for i, d1 in enumerate(drug_objects):
        eff1 = d1.get("microbiome_effects", {})
        dec1 = {e["bacteria"].lower(): e for e in eff1.get("decreases", [])}
        inc1 = {e["bacteria"].lower(): e for e in eff1.get("increases", [])}
        
        for d2 in drug_objects[i+1:]:
            eff2 = d2.get("microbiome_effects", {})
            dec2 = {e["bacteria"].lower(): e for e in eff2.get("decreases", [])}
            inc2 = {e["bacteria"].lower(): e for e in eff2.get("increases", [])}
            
            pair = [d1["drug_name"], d2["drug_name"]]
            
            # 2a: Compounding depletion of beneficial bacteria
            shared_decreases = set(dec1.keys()) & set(dec2.keys())
            beneficial_shared = [b for b in shared_decreases if b in BENEFICIAL_TAXA]
            if beneficial_shared:
                combined = sum(
                    MAGNITUDE_SCORE.get(dec1[b]["magnitude"], 1) + MAGNITUDE_SCORE.get(dec2[b]["magnitude"], 1)
                    for b in beneficial_shared
                )
                if combined >= 4:
                    severity = "high" if combined >= 6 else "moderate"
                else:
                    severity = "mild"
                
                bacteria_list = ", ".join(b.title() for b in beneficial_shared)
                key = (d1["drug_name"], d2["drug_name"], "compounding_depletion")
                if key not in seen:
                    seen.add(key)
                    explanation = (
                        f"Both {pair[0]} and {pair[1]} reduce beneficial {bacteria_list} levels. "
                        f"Taking them together may cause {severity} depletion of "
                        f"{'this protective species' if len(beneficial_shared) == 1 else 'these protective species'}, "
                        f"weakening gut health."
                    )
                    interactions.append({
                        "drugs": pair,
                        "interaction_type": "compounding_harm",
                        "type": "compounding_depletion",
                        "confidence": _compute_confidence([d1, d2], len(beneficial_shared)),
                        "affected_bacteria": beneficial_shared,
                        "combined_severity": severity,
                        "severity": severity,
                        "bacteria": beneficial_shared,
                        "explanation": explanation,
                        "description": explanation,
                        "recommendation": f"Consider targeted probiotic support for {bacteria_list} strains. Space medications apart if possible."
                    })
            
            # 2b: Compounding increase of harmful bacteria
            shared_increases = set(inc1.keys()) & set(inc2.keys())
            harmful_shared = [b for b in shared_increases if b in HARMFUL_TAXA]
            if harmful_shared:
                combined = sum(
                    MAGNITUDE_SCORE.get(inc1[b]["magnitude"], 1) + MAGNITUDE_SCORE.get(inc2[b]["magnitude"], 1)
                    for b in harmful_shared
                )
                severity = "high" if combined >= 6 else "moderate" if combined >= 4 else "mild"
                
                bacteria_list = ", ".join(b.title() for b in harmful_shared)
                key = (d1["drug_name"], d2["drug_name"], "compounding_overgrowth")
                if key not in seen:
                    seen.add(key)
                    explanation = (
                        f"{pair[0]} and {pair[1]} both encourage {bacteria_list} growth. "
                        f"Together, this creates a {severity} risk of overgrowth, "
                        f"which may lead to digestive issues or infections."
                    )
                    interactions.append({
                        "drugs": pair,
                        "interaction_type": "compounding_harm",
                        "type": "compounding_overgrowth",
                        "confidence": _compute_confidence([d1, d2], len(harmful_shared)),
                        "affected_bacteria": harmful_shared,
                        "combined_severity": severity,
                        "severity": severity,
                        "bacteria": harmful_shared,
                        "explanation": explanation,
                        "description": explanation,
                        "recommendation": f"Monitor for symptoms of {bacteria_list} overgrowth. Probiotic competition therapy may help."
                    })
            
            # 2c: Opposing effects (one increases what the other decreases)
            conflicts = []
            for bact in set(dec1.keys()) & set(inc2.keys()):
                dec_score = MAGNITUDE_SCORE.get(dec1[bact]["magnitude"], 1)
                inc_score = MAGNITUDE_SCORE.get(inc2[bact]["magnitude"], 1)
                conflicts.append({"bacteria": bact, "decreased_by": d1["drug_name"], "increased_by": d2["drug_name"], "score": dec_score + inc_score})
            for bact in set(dec2.keys()) & set(inc1.keys()):
                if bact not in {c["bacteria"] for c in conflicts}:
                    dec_score = MAGNITUDE_SCORE.get(dec2[bact]["magnitude"], 1)
                    inc_score = MAGNITUDE_SCORE.get(inc1[bact]["magnitude"], 1)
                    conflicts.append({"bacteria": bact, "decreased_by": d2["drug_name"], "increased_by": d1["drug_name"], "score": dec_score + inc_score})
            
            if conflicts:
                top = max(conflicts, key=lambda c: c["score"])
                total_score = sum(c["score"] for c in conflicts)
                severity = "moderate" if total_score >= 6 else "mild"
                
                bacteria_list = ", ".join(c["bacteria"].title() for c in conflicts)
                key = (d1["drug_name"], d2["drug_name"], "opposing")
                if key not in seen:
                    seen.add(key)
                    affected = [c["bacteria"] for c in conflicts]
                    explanation = (
                        f"{top['decreased_by']} may reduce the {top['bacteria'].title()} increase from "
                        f"{top['increased_by']}, potentially undermining its gut health benefits."
                        + (f" They also have opposing effects on {', '.join(c['bacteria'].title() for c in conflicts if c['bacteria'] != top['bacteria'])}." if len(conflicts) > 1 else "")
                    )
                    interactions.append({
                        "drugs": pair,
                        "interaction_type": "opposing_effects",
                        "type": "opposing_effects",
                        "confidence": _compute_confidence([d1, d2], len(conflicts)),
                        "affected_bacteria": affected,
                        "combined_severity": severity,
                        "severity": severity,
                        "bacteria": affected,
                        "explanation": explanation,
                        "description": explanation,
                        "recommendation": f"The net effect on {top['bacteria'].title()} is unpredictable. Discuss timing optimization with your pharmacist."
                    })
    
    # Sort by severity
    severity_order = {"critical": 0, "severe": 1, "significant": 2, "moderate": 3, "mild": 4}
    interactions.sort(key=lambda x: severity_order.get(x.get("severity", "mild"), 5))
    
    return interactions


# =============================================================================
# COMBINED MICROBIOME PREDICTION
# =============================================================================

# Shared scoring constants
_MAGNITUDE_SCORE = {"mild": 1, "moderate": 2, "significant": 3}

# Known harmful bacteria (increases are bad)
_HARMFUL_TAXA = {
    "enterococcus", "enterobacteriaceae", "clostridium difficile",
    "candida", "proteobacteria", "streptococcus",
    "erysipelotrichaceae", "desulfovibrionaceae",
}

# Known beneficial bacteria (decreases are bad)
_BENEFICIAL_TAXA = {
    "lactobacillus", "bifidobacterium", "akkermansia",
    "faecalibacterium", "roseburia", "coprococcus",
    "muribaculaceae", "allobaculum", "lactobacillus reuteri",
    "bifidobacterium longum",
}


def _parse_diversity_score(text: str) -> int:
    """Map free-text overall_diversity values to numeric scores.

    Scale: -3 (severely decreased) to +2 (increased/restored).
    """
    t = text.lower().strip()
    if "severely" in t:
        return -3
    if "significantly" in t:
        return -3
    if "moderately" in t:
        return -2
    if "restored" in t or "beneficial" in t:
        return 2
    if "increased" in t:
        return 2
    if "slight increase" in t:
        return 1
    if "mildly decreased" in t or "mildly beneficial" in t:
        return -1 if "decreased" in t else 1
    if "decreased" in t:
        return -2
    if "mild change" in t or "mild changes" in t:
        return -1
    # "minimal change" and everything else
    return 0


def _diversity_severity(score: int) -> str:
    """Map combined diversity score to a severity label."""
    if score <= -6:
        return "critical"
    if score <= -4:
        return "severe"
    if score <= -2:
        return "significant"
    if score <= -1:
        return "moderate"
    if score == 0:
        return "neutral"
    return "beneficial"


# Evidence strength scoring: higher = more confident
_EVIDENCE_SCORE = {"strong": 3, "moderate": 2, "emerging": 1, "limited": 0}


def _compute_confidence(drug_objects: list, shared_count: int) -> str:
    """Compute prediction confidence weighted by evidence strength.

    Rules:
    - Base confidence from shared bacteria count: 2+ = high, 1 = moderate
    - Evidence caps the result: if the weakest drug is 'emerging', cap at moderate;
      if 'limited', cap at low
    - Two 'strong' evidence drugs with 2+ shared bacteria = confirmed
    """
    evidence_levels = [
        d.get("microbiome_effects", {}).get("evidence_strength", "emerging")
        for d in drug_objects
    ]
    min_evidence = min(_EVIDENCE_SCORE.get(e, 0) for e in evidence_levels)

    # Base confidence from shared bacteria count
    if shared_count >= 2:
        base = "high"
    else:
        base = "moderate"

    # Evidence-based ceiling
    if min_evidence >= 3:  # all strong
        ceiling = "confirmed" if shared_count >= 2 else "high"
    elif min_evidence >= 2:  # weakest is moderate
        ceiling = "high"
    elif min_evidence >= 1:  # weakest is emerging
        ceiling = "moderate"
    else:  # limited
        ceiling = "low"

    # Return the lower of base and ceiling
    rank = {"confirmed": 4, "high": 3, "moderate": 2, "low": 1}
    result_rank = min(rank[base], rank[ceiling])
    return {4: "confirmed", 3: "high", 2: "moderate", 1: "low"}[result_rank]


def _score_to_severity(score: int) -> str:
    """Map combined magnitude score to severity level.

    Rules:
      1 → mild
      2 → moderate   (mild + mild)
      3 → significant (mild + moderate)
      4-5 → severe   (moderate + moderate, anything + significant)
      6+ → critical  (significant + significant, or 3+ drugs stacking)
    """
    if score <= 1:
        return "mild"
    elif score == 2:
        return "moderate"
    elif score == 3:
        return "significant"
    elif score <= 5:
        return "severe"
    else:
        return "critical"


def _explain_compounding_depletion(bacteria: str, drugs: list, severity: str) -> str:
    """Generate natural-language explanation for compounding depletion."""
    name = bacteria.title()
    if len(drugs) == 2:
        return (
            f"Both {drugs[0]} and {drugs[1]} reduce {name} levels in the gut. "
            f"Taking them together may cause {severity} depletion of this beneficial species, "
            f"weakening its protective effects on gut health."
        )
    return (
        f"{', '.join(drugs[:-1])}, and {drugs[-1]} all deplete {name}. "
        f"This {severity} combined impact could substantially reduce "
        f"your gut's supply of this protective bacterium."
    )


def _explain_compounding_overgrowth(bacteria: str, drugs: list, severity: str) -> str:
    """Generate natural-language explanation for compounding overgrowth."""
    name = bacteria.title()
    if len(drugs) == 2:
        return (
            f"{drugs[0]} and {drugs[1]} both encourage {name} growth. "
            f"Together, this creates a {severity} risk of overgrowth, "
            f"which may lead to digestive issues or infections."
        )
    return (
        f"{', '.join(drugs[:-1])}, and {drugs[-1]} all promote {name} growth. "
        f"The {severity} combined effect significantly raises overgrowth risk."
    )


def _explain_benefit_undermined(
    bacteria: str, helpers: list, underminers: list, net_effect: str
) -> str:
    """Generate natural-language explanation for benefit undermined."""
    name = bacteria.title()
    helper_str = " and ".join(helpers) if len(helpers) <= 2 else f"{', '.join(helpers[:-1])}, and {helpers[-1]}"
    underminer_str = " and ".join(underminers) if len(underminers) <= 2 else f"{', '.join(underminers[:-1])}, and {underminers[-1]}"

    if net_effect == "net_increased":
        outcome = f"The {name} benefit from {helper_str} still outweighs the reduction, but is diminished."
    elif net_effect == "neutral":
        outcome = f"The competing effects roughly cancel out, potentially neutralizing {helper_str}'s {name} benefit entirely."
    else:
        outcome = f"The reduction outweighs the benefit, meaning {helper_str}'s positive {name} effect may be largely lost."

    return (
        f"{underminer_str} may reduce the {name} increase from {helper_str}, "
        f"potentially undermining its gut health benefits. {outcome}"
    )


def _build_diversity_description(details, combined_score, severity):
    """Build a human-readable description of combined diversity impact."""
    neg = [d for d in details if d["score"] < 0]
    pos = [d for d in details if d["score"] > 0]
    if combined_score <= -4:
        return (
            f"Multiple medications ({', '.join(d['drug'] for d in neg)}) are reducing "
            f"gut microbiome diversity. Combined impact: {severity}. "
            f"Consider broad-spectrum probiotics and dietary fiber to counteract."
        )
    if combined_score <= -2:
        return (
            f"{', '.join(d['drug'] for d in neg)} {'is' if len(neg) == 1 else 'are'} "
            f"reducing diversity ({severity} impact). "
            f"Prebiotic and probiotic support recommended."
        )
    if combined_score < 0:
        return f"Mild diversity reduction from {', '.join(d['drug'] for d in neg)}."
    if combined_score == 0:
        if not pos and not neg:
            return "No significant diversity impact expected."
        return "Positive and negative diversity effects roughly cancel out."
    return (
        f"{', '.join(d['drug'] for d in pos)} {'is' if len(pos) == 1 else 'are'} "
        f"actively supporting microbiome diversity — a beneficial effect."
    )


def predict_microbiome(drugs: List[str]) -> Dict[str, Any]:
    """Analyze combined microbiome effects across all drugs.

    Takes a full drug list and returns:
    - Per-bacterium net effect with severity scored by combined magnitudes
    - Compounding depletions (multiple drugs hitting same beneficial bacteria)
    - Compounding overgrowth (multiple drugs boosting same harmful bacteria)
    - Beneficial cancellations (one drug's benefit undermined by another)
    - Overall microbiome health score
    """
    drug_objects = []
    for name in drugs:
        drug = find_drug(name)
        if drug:
            drug_objects.append(drug)

    if not drug_objects:
        return {
            "drugs_analyzed": [],
            "bacteria": [],
            "compounding_depletions": [],
            "compounding_overgrowth": [],
            "beneficial_cancellations": [],
            "overall_score": 0,
            "overall_severity": "neutral",
            "summary": "No recognized drugs provided.",
        }

    # --- Build per-bacterium map across ALL drugs ---
    drug_by_name = {d["drug_name"]: d for d in drug_objects}
    bacteria_map: Dict[str, Dict] = {}
    for drug in drug_objects:
        effects = drug.get("microbiome_effects", {})
        for entry in effects.get("decreases", []):
            bact = entry["bacteria"].lower()
            if bact not in bacteria_map:
                bacteria_map[bact] = {"decreased_by": [], "increased_by": []}
            bacteria_map[bact]["decreased_by"].append({
                "drug": drug["drug_name"],
                "magnitude": entry["magnitude"],
                "score": _MAGNITUDE_SCORE.get(entry["magnitude"], 1),
                "mechanism": entry.get("mechanism", ""),
            })
        for entry in effects.get("increases", []):
            bact = entry["bacteria"].lower()
            if bact not in bacteria_map:
                bacteria_map[bact] = {"decreased_by": [], "increased_by": []}
            bacteria_map[bact]["increased_by"].append({
                "drug": drug["drug_name"],
                "magnitude": entry["magnitude"],
                "score": _MAGNITUDE_SCORE.get(entry["magnitude"], 1),
                "mechanism": entry.get("mechanism", ""),
            })

    # --- Analyze each bacterium ---
    bacteria_results = []
    compounding_depletions = []
    compounding_overgrowth = []
    beneficial_cancellations = []
    synergistic_benefits = []

    for bact, data in bacteria_map.items():
        total_dec = sum(d["score"] for d in data["decreased_by"])
        total_inc = sum(d["score"] for d in data["increased_by"])
        net_score = total_dec - total_inc  # positive = net decrease
        is_beneficial = bact in _BENEFICIAL_TAXA
        is_harmful = bact in _HARMFUL_TAXA

        if net_score > 0:
            direction = "net_decreased"
        elif net_score < 0:
            direction = "net_increased"
        else:
            direction = "neutral"

        result = {
            "bacteria": bact,
            "display_name": bact.title(),
            "is_beneficial": is_beneficial,
            "is_harmful": is_harmful,
            "direction": direction,
            "net_score": net_score,
            "combined_severity": _score_to_severity(abs(net_score)),
            "drugs_decreasing": [d["drug"] for d in data["decreased_by"]],
            "drugs_increasing": [d["drug"] for d in data["increased_by"]],
            "decrease_total": total_dec,
            "increase_total": total_inc,
        }
        bacteria_results.append(result)

        # Compounding depletion: 2+ drugs decrease a beneficial bacterium
        if is_beneficial and len(data["decreased_by"]) >= 2:
            drug_list = [d["drug"] for d in data["decreased_by"]]
            sev = _score_to_severity(total_dec)
            compounding_depletions.append({
                "interaction_type": "compounding_harm",
                "affected_bacteria": bact,
                "display_name": bact.title(),
                "confidence": _compute_confidence(
                    [drug_by_name[d] for d in drug_list if d in drug_by_name],
                    len(drug_list)  # multiple drugs confirming same effect
                ),
                "combined_severity": sev,
                "severity": sev,
                "combined_score": total_dec,
                "drugs": drug_list,
                "drug_details": data["decreased_by"],
                "explanation": _explain_compounding_depletion(bact, drug_list, sev),
                "description": (
                    f"{', '.join(drug_list)} all reduce "
                    f"beneficial {bact.title()}. Combined severity: {sev}."
                ),
                "recommendation": (
                    f"Consider targeted probiotic with {bact.title()} strains. "
                    f"Space medications apart to reduce compounding impact."
                ),
            })

        # Compounding overgrowth: 2+ drugs increase a harmful bacterium
        if is_harmful and len(data["increased_by"]) >= 2:
            drug_list = [d["drug"] for d in data["increased_by"]]
            sev = _score_to_severity(total_inc)
            compounding_overgrowth.append({
                "interaction_type": "compounding_harm",
                "affected_bacteria": bact,
                "display_name": bact.title(),
                "confidence": _compute_confidence(
                    [drug_by_name[d] for d in drug_list if d in drug_by_name],
                    len(drug_list)
                ),
                "combined_severity": sev,
                "severity": sev,
                "combined_score": total_inc,
                "drugs": drug_list,
                "drug_details": data["increased_by"],
                "explanation": _explain_compounding_overgrowth(bact, drug_list, sev),
                "description": (
                    f"{', '.join(drug_list)} all promote "
                    f"harmful {bact.title()} growth. Combined severity: {sev}."
                ),
                "recommendation": (
                    f"Monitor for {bact.title()} overgrowth symptoms. "
                    f"Competitive probiotic therapy may help."
                ),
            })

        # Beneficial cancellation: a drug increases a beneficial bacterium
        # but another drug decreases it, undermining the benefit
        if is_beneficial and data["increased_by"] and data["decreased_by"]:
            helpers = [d["drug"] for d in data["increased_by"]]
            underminers = [d["drug"] for d in data["decreased_by"]]
            sev = _score_to_severity(total_dec)
            beneficial_cancellations.append({
                "interaction_type": "benefit_undermined",
                "affected_bacteria": bact,
                "display_name": bact.title(),
                "confidence": _compute_confidence(
                    [drug_by_name[d] for d in (helpers + underminers) if d in drug_by_name],
                    len(helpers) + len(underminers)
                ),
                "combined_severity": sev,
                "severity": sev,
                "net_effect": direction,
                "net_score": net_score,
                "drugs_helping": helpers,
                "drugs_undermining": underminers,
                "help_score": total_inc,
                "undermine_score": total_dec,
                "explanation": _explain_benefit_undermined(
                    bact, helpers, underminers, direction
                ),
                "description": (
                    f"{', '.join(helpers)} {'increases' if len(helpers) == 1 else 'increase'} "
                    f"beneficial {bact.title()}, but {', '.join(underminers)} "
                    f"{'decreases' if len(underminers) == 1 else 'decrease'} it. "
                    f"{'The benefit is being undermined.' if net_score > 0 else 'The benefit partially survives.' if net_score == 0 else 'The benefit still outweighs the harm.'}"
                ),
                "recommendation": (
                    f"Consider spacing {', '.join(underminers)} away from {', '.join(helpers)} to preserve "
                    f"{bact.title()} benefits. Timing optimization may help both drugs work."
                ),
            })

        # Synergistic benefit: 2+ drugs increase the same beneficial bacterium
        if is_beneficial and len(data["increased_by"]) >= 2 and not data["decreased_by"]:
            drug_list = [d["drug"] for d in data["increased_by"]]
            sev = _score_to_severity(total_inc)
            drug_str = " and ".join(drug_list) if len(drug_list) <= 2 else f"{', '.join(drug_list[:-1])}, and {drug_list[-1]}"
            synergistic_benefits.append({
                "interaction_type": "synergistic_benefit",
                "affected_bacteria": bact,
                "confidence": _compute_confidence(
                    [drug_by_name[d] for d in drug_list if d in drug_by_name],
                    len(drug_list)
                ),
                "display_name": bact.title(),
                "combined_severity": sev,
                "combined_score": total_inc,
                "drugs": drug_list,
                "drug_details": data["increased_by"],
                "explanation": (
                    f"{drug_str} both promote {bact.title()} growth, creating a synergistic "
                    f"boost to this beneficial species. This {sev} combined effect strengthens "
                    f"gut health beyond what either medication achieves alone."
                ),
            })

    # Sort results: worst concerns first
    severity_order = {"critical": 0, "severe": 1, "significant": 2, "moderate": 3, "mild": 4}
    bacteria_results.sort(key=lambda b: severity_order.get(b["combined_severity"], 5))
    compounding_depletions.sort(key=lambda c: -c["combined_score"])
    compounding_overgrowth.sort(key=lambda c: -c["combined_score"])
    beneficial_cancellations.sort(key=lambda c: -c["undermine_score"])
    synergistic_benefits.sort(key=lambda c: -c["combined_score"])

    # --- Diversity impact ---
    diversity_details = []
    for drug in drug_objects:
        raw = drug.get("microbiome_effects", {}).get("overall_diversity", "")
        score = _parse_diversity_score(raw) if raw else 0
        diversity_details.append({
            "drug": drug["drug_name"],
            "raw_value": raw,
            "score": score,
        })
    combined_diversity_score = sum(d["score"] for d in diversity_details)
    diversity_severity = _diversity_severity(combined_diversity_score)

    diversity_impact = {
        "per_drug": diversity_details,
        "combined_score": combined_diversity_score,
        "severity": diversity_severity,
        "description": _build_diversity_description(diversity_details, combined_diversity_score, diversity_severity),
    }

    # Overall microbiome health score
    concern_total = (
        sum(c["combined_score"] for c in compounding_depletions)
        + sum(c["combined_score"] for c in compounding_overgrowth)
        + sum(c["undermine_score"] for c in beneficial_cancellations)
    )
    # Factor in diversity: negative diversity adds to concerns
    if combined_diversity_score < 0:
        concern_total += abs(combined_diversity_score)
    benefit_total = sum(
        b["increase_total"] for b in bacteria_results
        if b["is_beneficial"] and b["direction"] == "net_increased"
    ) + sum(
        b["decrease_total"] for b in bacteria_results
        if b["is_harmful"] and b["direction"] == "net_decreased"
    )
    # Positive diversity counts as benefit
    if combined_diversity_score > 0:
        benefit_total += combined_diversity_score
    overall_score = concern_total - benefit_total

    if overall_score <= 0:
        overall_severity = "beneficial" if benefit_total > 0 else "neutral"
    else:
        overall_severity = _score_to_severity(overall_score)

    # Build summary
    drug_names = [d["drug_name"] for d in drug_objects]
    parts = []
    if compounding_depletions:
        worst = compounding_depletions[0]
        parts.append(
            f"{worst['display_name']} is hit hardest — {len(worst['drugs'])} drugs "
            f"combine for {worst['severity']} depletion"
        )
    if beneficial_cancellations:
        worst = beneficial_cancellations[0]
        parts.append(
            f"{', '.join(worst['drugs_undermining'])} may undermine "
            f"{', '.join(worst['drugs_helping'])}'s {worst['display_name']} benefit"
        )
    if compounding_overgrowth:
        worst = compounding_overgrowth[0]
        parts.append(
            f"{worst['display_name']} overgrowth risk from {len(worst['drugs'])} drugs"
        )
    if diversity_severity in ("severe", "critical"):
        parts.append(
            f"Combined diversity loss is {diversity_severity}"
        )
    elif diversity_severity == "significant":
        parts.append("Notable diversity reduction across medications")
    if synergistic_benefits and not compounding_depletions and not beneficial_cancellations:
        bact_names = [s["display_name"] for s in synergistic_benefits]
        drug_set = sorted({d for s in synergistic_benefits for d in s["drugs"]})
        parts.append(
            f"{' and '.join(drug_set)} work together to boost {', '.join(bact_names)}"
        )
    if diversity_severity == "beneficial" and not parts:
        parts.append("Your medications synergistically support microbiome diversity")
    if not parts:
        parts.append("Your medications have minimal combined microbiome interactions")

    return {
        "drugs_analyzed": drug_names,
        "bacteria": bacteria_results,
        "compounding_depletions": compounding_depletions,
        "compounding_overgrowth": compounding_overgrowth,
        "beneficial_cancellations": beneficial_cancellations,
        "synergistic_benefits": synergistic_benefits,
        "diversity_impact": diversity_impact,
        "overall_score": overall_score,
        "overall_severity": overall_severity,
        "summary": ". ".join(parts) + ".",
    }
