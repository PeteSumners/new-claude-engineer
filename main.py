import asyncio
import json
import os
import sys
import subprocess
from ai_service import AIService
from tool_service import ToolService

def setup():
    required_packages = ['anthropic', 'asyncio']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print("Setup complete.")

class ClaudeEngineer:
    def __init__(self, api_key):
        self.ai_service = AIService(api_key)
        self.tool_service = ToolService()
        self.state = {
            "conversation_history": [],
            "completed_tasks": [],
            "in_progress_tasks": ["Implement project continuity features"],
            "planned_tasks": [
                "Implement more sophisticated AI model",
                "Add more tools to ToolService",
                "Create advanced parsing system for user inputs",
                "Develop web-based or GUI interface",
                "Implement user authentication and personalization"
            ]
        }

    def save_state(self):
        with open("project_state.json", "w") as f:
            json.dump(self.state, f, indent=4)

    def load_state(self):
        try:
            with open("project_state.json", "r") as f:
                self.state = json.load(f)
        except FileNotFoundError:
            print("No existing state found. Starting with a new state.")

    async def process_request(self, user_input: str) -> str:
        # First, get a response from the AI service
        ai_response = await self.ai_service.generate_response(user_input)
        
        # Then, use the tool service to echo the AI's response
        tool_response = self.tool_service.execute_tool("echo", ai_response)
        
        # Update the conversation history in the state
        if "conversation_history" not in self.state:
            self.state["conversation_history"] = []
        
        self.state["conversation_history"].append({
            "user_input": user_input,
            "ai_response": ai_response,
            "tool_response": tool_response
        })
        
        return f"AI Response: {ai_response}\nTool Response: {tool_response}"

def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
    else:
        print("Warning: .env file not found.")

def get_api_key():
    load_env()
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("Anthropic API key not found in .env file")
    return api_key

async def main():
    setup()
    load_env()
    try:
        api_key = get_api_key()
        claude = ClaudeEngineer(api_key)
        claude.load_state()  # Load the state at startup
        
        interaction_count = 0
        while True:
            user_input = input("User: ")
            if user_input.lower() == "exit":
                break
            
            response = await claude.process_request(user_input)
            print(f"Claude Engineer: {response}")
            
            interaction_count += 1
            if interaction_count % 5 == 0:  # Save state every 5 interactions
                claude.save_state()
                print("Project state saved.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        # Save state before exiting
        if 'claude' in locals():
            claude.save_state()
        print("Final project state saved. Goodbye!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {str(e)}")