import asyncio
from mcp_core.chat import chat_main

if __name__ == "__main__":
    asyncio.run(chat_main(
        server_config_path="server_config.json",
        provider="ollama",
        model_name="llama3.2"
    ))

