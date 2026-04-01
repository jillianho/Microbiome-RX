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
    """Check for interactions between multiple drugs."""
    interactions = []
    drug_classes = []
    
    # Get classes for each drug
    for drug_name in drugs:
        drug = find_drug(drug_name)
        if drug:
            drug_classes.append((drug_name, drug["drug_class"].lower().split()[0]))
    
    # Check pairwise interactions
    for i, (drug1, class1) in enumerate(drug_classes):
        for drug2, class2 in drug_classes[i+1:]:
            # Check known interactions
            for (c1, c2), interaction in DRUG_INTERACTIONS.items():
                if (c1 in class1 and c2 in class2) or (c2 in class1 and c1 in class2):
                    interactions.append({
                        "drugs": [drug1, drug2],
                        **interaction
                    })
    
    return interactions
