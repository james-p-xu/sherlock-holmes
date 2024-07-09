from openai import OpenAI


def GPT4oResponse(system_prompt, user_content):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-2024-05-13",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
    )

    return completion.choices[0].message


def GPT4TurboResponse(system_prompt, user_content):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
    )

    return completion.choices[0].message
