# Claude Engineer

Claude Engineer is a simple AI-powered assistant that combines natural language processing with basic tool functionality.

## Components

### 1. AIService

The AIService is responsible for generating responses to user inputs. Currently, it uses a mock implementation that simply echoes the user's input.

Key features:
- Asynchronous `generate_response` method
- Mock implementation for demonstration purposes

### 2. ToolService

The ToolService manages and executes various tools. Currently, it only has an "echo" tool implemented.

Key features:
- `execute_tool` method to run specified tools
- Error handling for unknown tools
- Extendable design for adding more tools in the future

### 3. ClaudeEngineer

The main class that integrates AIService and ToolService to process user requests.

Key features:
- Combines AI-generated responses with tool execution
- Provides a simple command-line interface for user interaction

## Usage

To use Claude Engineer, run the `main.py` script:

```
python main.py
```

Enter your queries when prompted. Type "exit" to end the session.

## Project Structure

- `main.py`: The main script that runs the Claude Engineer
- `ai_service.py`: Contains the AIService class
- `tool_service.py`: Contains the ToolService class
- `test_ai_service.py`: Unit tests for AIService
- `test_tool_service.py`: Unit tests for ToolService

## Testing

To run the tests, execute the test files:

```
python test_ai_service.py
python test_tool_service.py
```

## Future Improvements

1. Implement more sophisticated AI responses
2. Add more tools to the ToolService
3. Create more complex interactions between the AI and tools
4. Improve error handling and user feedback
5. Add configuration options for customization