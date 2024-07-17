import unittest
from tool_service import ToolService

class TestToolService(unittest.TestCase):
    def setUp(self):
        self.tool_service = ToolService()

    def test_echo_tool(self):
        message = "Hello, World!"
        result = self.tool_service.execute_tool("echo", message)
        self.assertEqual(result, f"Echo: {message}")

    def test_unknown_tool(self):
        result = self.tool_service.execute_tool("unknown_tool")
        self.assertEqual(result, "Error: Tool 'unknown_tool' not found.")

if __name__ == '__main__':
    unittest.main()