import os
import anthropic

class AIService:
    def __init__(self, api_key: str):
        """
        Initialize the AIService with the Anthropic client.
        
        :param api_key: The Anthropic API key
        """
        self.client = anthropic.Anthropic(api_key=api_key)

    async def generate_response(self, user_input: str) -> str:
        """
        Generate a response using Claude 3.5 Sonnet model.
        
        :param user_input: The user's input message
        :return: The generated response from Claude
        """
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                temperature=0.7,
                system="You are Claude, an AI assistant created by Anthropic to be helpful, harmless, and honest.",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            return response.content[0].text
        except anthropic.APIError as e:
            print(f"An error occurred: {e}")
            return "I apologize, but I encountered an error while processing your request. Please try again later."
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "I apologize, but an unexpected error occurred. Please try again later."