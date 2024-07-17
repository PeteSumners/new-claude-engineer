import asyncio
from ai_service import AIService
from tool_service import ToolService

class ClaudeEngineer:
    def __init__(self):
        self.ai_service = AIService()
        self.tool_service = ToolService()

    async def process_request(self, user_input: str) -> str:
        # First, get a response from the AI service
        ai_response = await self.ai_service.generate_response(user_input)
        
        # Then, use the tool service to echo the AI's response
        tool_response = self.tool_service.execute_tool("echo", ai_response)
        
        return f"AI Response: {ai_response}\nTool Response: {tool_response}"

async def main():
    claude = ClaudeEngineer()
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = await claude.process_request(user_input)
        print(f"Claude Engineer: {response}")

if __name__ == "__main__":
    asyncio.run(main())