# client_fixed.py
import asyncio
from fastmcp import Client

async def main():
    # 直接连到已经在跑的 HTTP 服务地址（注意带 /mcp）
    client = Client("http://127.0.0.1:8002/sse")

    async with client:
        await client.ping()
        tools = await client.list_tools()
        print("tools:", tools)
        # 参数按服务定义，转成字符串更稳妥（你的服务把参数 Annotated 为 str）
        result = await client.call_tool("add", {"a": "937434", "b": "24689"})
        print("result:", result)

if __name__ == "__main__":
    asyncio.run(main())
