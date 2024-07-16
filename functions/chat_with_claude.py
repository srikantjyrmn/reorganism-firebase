import os
import anthropic
from openai import OpenAI

def chat_with_Openai(message):
    # Get the API key from environment variable
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("OPENAI_API_KEY not found in environment variables")
        return "OPENAI_API_KEY not found in environment variables"

    print(f"API Key found: {api_key[:5]}...") # Print first 5 characters for verification

    # Set the OpenAI API key
    openai.api_key = api_key

    try:
        print("Sending request to OpenAI API...")
        response = OpenAI.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a world-class poet. Respond only with short poems."},
                {"role": "user", "content": message}
            ],
            max_tokens=1000,
            temperature=0.5
        )
        print("Successfully received response from OpenAI API")
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error in OpenAI API request: {e}")
        return f"Error in OpenAI API request: {e}"

def chat_with_Claude(message):
    # Get the API key from environment variable
    api_key = os.environ.get('CLAUDE_API_KEY')
    if not api_key:
        print("CLAUDE_API_KEY not found in environment variables")
        return "CLAUDE_API_KEY not found in environment variables"

    print(f"API Key found: {api_key[:5]}...") # Print first 5 characters for verification

    # Create an instance of the Anthropics client
    client = anthropic.Anthropic(api_key=api_key)

    try:
        print("Sending request to Claude API...")
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are a world-class poet. Respond only with short poems.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": message
                        }
                    ]
                }
            ]
        )
        print("Successfully received response from Claude API")
        return response.content
    except Exception as e:
        print(f"Error in Claude API request: {e}")
        return f"Error in Claude API request: {e}"

# Example usage
if __name__ == "__main__":
    user_message = "Why is the ocean salty?"
    response = chat_with_Claude(user_message)
    print(response)
