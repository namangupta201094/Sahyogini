import logging
import openai

logger = logging.getLogger(__name__)

class LLMInterface:
    def __init__(self):
        self.api_key = "your-openai-api-key"  # Replace with your actual OpenAI API key
        openai.api_key = self.api_key

    def generate_response(self, prompt, context):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"{context}\n\nUser: {prompt}\nAI:",
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            logger.error(f"Error generating LLM response: {e}")
            return "I'm sorry, I'm having trouble generating a response right now. Please try again later."

    def personalize_response(self, response, user_profile):
        # Here you would implement logic to personalize the response based on the user profile
        # This is a placeholder implementation
        return f"Based on your profile as a {user_profile['occupation']} from {user_profile['location']}, here's a personalized response: {response}"
