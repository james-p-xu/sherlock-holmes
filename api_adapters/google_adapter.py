import os

import vertexai
from vertexai.generative_models import GenerativeModel


# Gemini-Advanced is currently unavailable through Google's API.
def Gemini1_5ProResponse(system_prompt, user_content):
    project_id = os.environ["GEMINI_PROJECT_ID"]
    vertexai.init(project=project_id)

    model = GenerativeModel(
        model="gemini-1.5-pro",
        system_instruction=[system_prompt]
    )

    response = model.generate_content([user_content])

    return response.text
