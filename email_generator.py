import google.generativeai as genai
from prompts.prompts import EMAIL_PROMPT


def generate_email(recipient, purpose, tone):

    prompt = EMAIL_PROMPT.format(
        recipient=recipient,
        purpose=purpose,
        tone=tone
    )

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text