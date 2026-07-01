import google.generativeai as genai
from prompts.prompts import SUMMARY_PROMPT


def summarize_email(text):

    prompt = SUMMARY_PROMPT.format(
        text=text
    )

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text