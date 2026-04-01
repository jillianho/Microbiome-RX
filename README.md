# MicrobiomeRx 💊🦠

**Drug-Microbiome Interaction Analyzer**

MicrobiomeRx is a tool that analyzes how medications alter the gut microbiome and translates those effects into actionable mental and physical health insights.

## Features

- **Drug Search**: Autocomplete search for medications by generic or brand name
- **Multi-Drug Analysis**: Analyze interactions between multiple medications
- **Bacteria Effects**: See which gut bacteria are increased/decreased
- **Mental Health Impact**: Understand gut-brain axis effects
- **Physical Health Impact**: GI, immune, metabolic effects
- **Drug Interactions**: Via microbiome pathways
- **Personalized Recommendations**: Probiotics, diet, timing suggestions

## Research Basis

Data derived from peer-reviewed research:

1. **Maier L, et al. (2018)** "Extensive impact of non-antibiotic drugs on human gut bacteria." *Nature* 555:623-628.
2. **Imhann F, et al. (2016)** "Proton pump inhibitors affect the gut microbiome." *Gut* 65:740-748.
3. **Vich Vila A, et al. (2020)** "Impact of commonly used drugs on the composition and metabolic function of the gut microbiota." *Nature Communications* 11:362.
4. **Flowers SA, et al. (2019)** "The microbiome in mental health." *Pharmacotherapy* 39(7):751-762.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Vanilla HTML/JS + Tailwind CSS
- **AI**: Claude API for personalized recommendations (optional)
- **Deployment**: Render

## Drugs in Database

- **PPIs**: Omeprazole, Esomeprazole
- **SSRIs**: Sertraline, Escitalopram, Fluoxetine
- **NSAIDs**: Ibuprofen, Naproxen, Aspirin
- **Antibiotics**: Amoxicillin, Azithromycin, Ciprofloxacin
- **Diabetes**: Metformin
- **Statins**: Atorvastatin
- **Others**: Alprazolam, Oxycodone, Oral Contraceptives

## Local Development

```bash
cd microbiome-rx/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Optional: for AI recommendations
export ANTHROPIC_API_KEY="your-key-here"

uvicorn main:app --reload --port 8000
```

Open: http://localhost:8000

## Deployment (Render)

1. Push to GitHub
2. Create Web Service on Render
3. Add `ANTHROPIC_API_KEY` env var (optional)
4. Deploy!

## Disclaimer

⚕️ **This tool is for educational purposes only.**

Not intended for clinical decision-making. The information provided does not constitute medical advice. Always consult your healthcare provider before making changes to your medication regimen.

## License

MIT
