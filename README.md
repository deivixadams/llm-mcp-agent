# 🧠 LLM-MCP Agent: Agente conversacional con herramientas inteligentes vía MCP

Este proyecto implementa un agente conversacional basado en **modelos de lenguaje locales (Ollama)** que interactúa dinámicamente con **herramientas externas expuestas mediante el protocolo [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)**.

A través de una arquitectura modular, el agente puede:

- 🔧 Invocar herramientas de procesamiento de cadenas (`StringTools`)
- 🕒 Consultar información temporal (`DateTimeTools`)
- 📂 Leer, escribir y listar archivos reales del sistema (`FileSystemTools`)
- 🧠 Resolver consultas en lenguaje natural y actuar en consecuencia

El sistema está construido con:

- [`LangGraph`](https://github.com/langchain-ai/langgraph) y agentes ReAct
- [`LangChain`](https://github.com/langchain-ai/langchain) + Ollama
- Herramientas MCP integradas como microservidores aislados
- Soporte para comandos personalizados como `/list_tools`

---

## 🚀 ¿Para qué sirve?

Esta arquitectura sirve como **plantilla funcional para agentes cognitivos** que:

- Pueden ampliar su conocimiento operativo con herramientas externas
- Ejecutan tareas reales sobre el sistema sin intervención humana
- Están listos para ser desplegados, integrados o personalizados

Ideal para desarrolladores, investigadores o educadores que deseen **construir agentes inteligentes que realmente actúan** sobre su entorno.

---

## 📦 Estructura del proyecto

```plaintext
📁 mcp_core/             # Núcleo de configuración y agentes
📄 main_chat.py          # Interfaz principal conversacional
🛠 server_config.json     # Configuración MCP de herramientas
📂 sandbox/              # Espacio seguro de trabajo para archivos



📝 Cualquier uso público, académico o comercial de este software debe incluir un reconocimiento visible y explícito a su autor original: PensamientoAumentado (shgcifrado@gmail.com).