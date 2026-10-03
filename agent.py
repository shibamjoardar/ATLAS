from openai import OpenAI
from tools import calculator

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL = "llama3.2"


# Tell ATLAS what tools are available
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform basic mathematical calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    },
                    "operation": {
                        "type": "string",
                        "enum": [
                            "add",
                            "subtract",
                            "multiply",
                            "divide"
                        ],
                        "description": "Mathematical operation"
                    }
                },
                "required": ["a", "b", "operation"]
            }
        }
    }
]


def ask_agent(prompt):

    messages = [
        {
            "role": "system",
            "content": """
You are ATLAS, an AI agent.

You can use tools when they are useful.
For mathematical calculations, use the calculator tool.
After receiving a tool result, explain the answer clearly to the user.
"""
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    while True:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools
        )

        message = response.choices[0].message

        # If ATLAS doesn't need a tool
        if not message.tool_calls:
            return message.content

        # Add ATLAS's response to conversation
        messages.append(message)

        # Execute requested tools
        for tool_call in message.tool_calls:

            if tool_call.function.name == "calculator":

                import json

                arguments = json.loads(
                    tool_call.function.arguments
                )

                result = calculator(
                    arguments["a"],
                    arguments["b"],
                    arguments["operation"]
                )

                # Give result back to ATLAS
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })