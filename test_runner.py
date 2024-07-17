import unittest
import asyncio
from ai_service import AIService

class TestAIService(unittest.TestCase):
    def setUp(self):
        self.ai_service = AIService()

    def test_generate_response(self):
        user_input = "Hello, Claude!"
        expected_response = f"You said: {user_input}. This is a mock response from the AI Service."
        
        # Run the coroutine in an event loop
        actual_response = asyncio.run(self.ai_service.generate_response(user_input))
        
        self.assertEqual(actual_response, expected_response)

    def test_generate_response_empty_input(self):
        user_input = ""
        expected_response = f"You said: {user_input}. This is a mock response from the AI Service."
        
        # Run the coroutine in an event loop
        actual_response = asyncio.run(self.ai_service.generate_response(user_input))
        
        self.assertEqual(actual_response, expected_response)

if __name__ == '__main__':
    unittest.main()