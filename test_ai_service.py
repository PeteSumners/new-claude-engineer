import pytest
from ai_service import AIService

@pytest.mark.asyncio
async def test_ai_service_generate_response():
    ai_service = AIService()
    user_input = "Hello, Claude!"
    response = await ai_service.generate_response(user_input)
    assert response == f"You said: {user_input}. This is a mock response from the AI Service."

@pytest.mark.asyncio
async def test_ai_service_generate_response_empty_input():
    ai_service = AIService()
    user_input = ""
    response = await ai_service.generate_response(user_input)
    assert response == f"You said: {user_input}. This is a mock response from the AI Service."