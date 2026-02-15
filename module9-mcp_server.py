from mcp.server.fastmcp import FastMCP
from langchain_community.tools import DuckDuckGoSearchRun

mcp = FastMCP("Demo Server")

@mcp.tool()
def calculator(oper1: int, oper2: int, operator: str) -> str:
    """Useful when you need to answer questions that involve adding, subtracting, multiplying, and dividing two numbers."""
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return float(a / b)
    
    if operator == '+' or operator == 'add':
        return str(add(oper1, oper2))
    elif operator == '-' or operator == 'subtract':
        return str(subtract(oper1, oper2))
    elif operator == '*' or operator == 'multiply':
        return str(multiply(float(oper1), float(oper2)))
    elif operator == '/' or operator == 'divide':
        return str(divide(oper1, oper2))
    else:
        return "Invalid operator"

@mcp.tool()
def duckduckgo_search(query: str) -> str:
    """Useful when you need to search the internet and find current information."""
    tool = DuckDuckGoSearchRun()
    result = tool.invoke(query)
    return result

if __name__ == "__main__":
    mcp.run()
