import google.generativeai as genai
from prompts.prompts import COVER_LETTER_PROMPT


def generate_cover_letter(name, position, company, skills):

    prompt = COVER_LETTER_PROMPT.format(
        name=name,
        position=position,
        company=company,
        skills=skills
    )

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text