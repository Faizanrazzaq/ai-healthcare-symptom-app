# AI Healthcare Symptom Information App

## Project overview
This project is a small educational healthcare application. A user enters a symptom description, and the app checks for a limited set of predefined phrases to show general health information.

## Innovation and motivation
Digital symptom information tools illustrate one way software can help people navigate health information. This prototype demonstrates a simple, transparent baseline; it is not a clinical AI system and does not use a trained machine-learning model or a large language model.

## Features
- Text input for a symptom description
- Basic case-insensitive phrase matching
- General informational guidance for a few example symptoms
- Safety disclaimer and emergency-care reminders
- Comments explaining the matching logic

## Technology
- Python
- Streamlit

## Run locally
1. Install Python 3.10 or newer.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   streamlit run app.py
   ```

## Testing checklist
- Submit an empty input and verify that a prompt appears.
- Enter `I have a cough and sore throat` and verify that matching guidance appears.
- Enter `chest pain` and verify that the app advises emergency medical care.
- Enter an unrelated phrase and verify that the app says no matching phrase was found.

## Limitations, safety, and ethics
- This is a rule-based educational prototype, not a diagnostic or validated triage tool.
- Phrase matching can miss symptoms, misunderstand context, and produce incomplete information.
- The guidance is not personalized and has not been clinically validated.
- Do not enter identifying or sensitive information.
- Never use this prototype to decide whether to delay professional or emergency care.

## References for further research
- U.S. Food and Drug Administration (FDA), Digital Health: https://www.fda.gov/medical-devices/digital-health-center-excellence
- World Health Organization (WHO), Ethics and governance of artificial intelligence for health: https://www.who.int/publications/i/item/9789240029200
- Streamlit documentation: https://docs.streamlit.io/

These references are starting points for research and are not evidence that this prototype is medically validated.
