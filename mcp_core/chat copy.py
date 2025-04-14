import asyncio
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langchain_core.runnables import Runnable
from langchain_core.tools import Tool

from mcp_core.ollama_provider import load_model
from mcp_core.config_loader import load_server_config
from langchain_mcp_adapters.client import MultiServerMCPClient

async def chat_main(
    server_config_path: str,
    provider: str = "ollama",
    model_name: str = "llama3.2"
):
    # 1️⃣ Cargar configuración de servidores MCP
    config = load_server_config(server_config_path)

    # 2️⃣ Cargar modelo
    model = load_model(model_name)

    # 3️⃣ Crear cliente MCP y descubrir herramientas
    async with MultiServerMCPClient(config) as client:
        tools: list[Tool] = client.get_tools()

        # 4️⃣ Crear el agente ReAct con el modelo y las herramientas
        agent: Runnable = create_react_agent(model, tools)

        print("\n🤖 MCP Chat iniciado. Escribe tu pregunta (Ctrl+C para salir):\n")
        while True:
            try:
                query = input("🧠 Tú: ").strip()
                if not query:
                    continue

                messages = [HumanMessage(content=query)]
                result = await agent.ainvoke({"messages": messages})

                for msg in result["messages"]:
                    print("🤖 Modelo:", msg.content)

                    print("🔧 Depuración------>")
                    
                    print("🤖 Mensaje completo:", msg.dict())

            except KeyboardInterrupt:
                print("\n👋 Chat finalizado.")
                break
