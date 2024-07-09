import anthropic


def ClaudeResponse(system_prompt, user_content, max_tokens=2048):
    client = anthropic.Anthropic()
    
    response = client.messages.create(
        model = "claude-3-5-sonnet-20240620",
        max_tokens = max_tokens,
        system = system_prompt,
        messages = [
            {"role": "user", "content": user_content}
        ]
    )

    return response.content
