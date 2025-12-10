from typing import Annotated
from fastmcp import FastMCP


mcp = FastMCP(name="AddServer")

@mcp.tool
def add(
    a: Annotated[str, "First number to add"],
    b: Annotated[str, "Second number to add"],
) -> int:
    """
    Return the sum of two numbers.
    """
    return int(a) + int(b)


if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8002)