class ToolService:
    def __init__(self):
        self.tools = {
            "echo": self.echo_tool
        }

    def execute_tool(self, tool_name: str, *args, **kwargs):
        if tool_name in self.tools:
            return self.tools[tool_name](*args, **kwargs)
        else:
            return f"Error: Tool '{tool_name}' not found."

    def echo_tool(self, message: str):
        return f"Echo: {message}"