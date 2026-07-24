import json


def parse_gemini_response(response_text):
    """
    Cleans Gemini response and converts it into a Python dictionary.
    """

    response_text = response_text.strip()

    # Remove markdown if Gemini returns it
    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    response_text = response_text.strip()

    return json.loads(response_text)