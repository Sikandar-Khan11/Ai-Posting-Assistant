import google.generativeai as genai
from prompts.prompts import LINKEDIN_PROMPT


def generate_linkedin(topic, achievement, tone):

    prompt = LINKEDIN_PROMPT.format(
        topic=topic,
        achievement=achievement,
        tone=tone
    )

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text