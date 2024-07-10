import os

from groq import Groq


def Llama3Response(system_prompt, user_content, max_tokens=2048, temperature=0.7):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    system_prompt = {
        "role": "system",
        "content": system_prompt
    }
    user_content = {
        "role": "user",
        "content": user_content
    }

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[system_prompt, user_content],
        max_tokens=max_tokens,
        temperature=temperature
    )

    return response.choices[0].message.content
