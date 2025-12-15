import asyncio
from fastmcp import Client

async def main():
    client = Client("http://127.0.0.1:8003/sse")

    async with client:
        # 检查服务器
        await client.ping()

        # 列出所有 tool
        tools = await client.list_tools()
        print("Tools:", tools)

        # 调用你定义的工具
        result = await client.call_tool(
            "get_kwc_code_examples", 
            {"query": "kd-checkbox", "k": 1}
        )
        print("Result:", result.content[0].text)

asyncio.run(main())
