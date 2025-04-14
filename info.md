# LangGraph + MCP + Ollama = Plug-n-play AI agents with real-world utility

## Git
git add . && git commit -m "🚀 Actualización: README completo, licencia con atribución y funcionalidad final MCP" && git push origin main


## Estructura

┌────────────┐
│   Usuario  │
└────┬───────┘
     │
     │ 1. Escribe pregunta natural
     ▼
┌──────────────┐
│   Chat Main  │
└────┬─────────┘
     │
     │ 2. Recibe input y lo pasa al agente
     ▼
┌──────────────────┐
│  LangGraph Agent │
└────┬─────────────┘
     │
     │ 3. Pasa input al modelo LLM (Ollama)
     ▼
┌──────────────┐
│    LLM       │
│ (llama3.2)   │
└────┬─────────┘
     │
     │ 4. Decide invocar una herramienta
     ▼
┌──────────────────────────┐
│  Tool Call (e.g. count_words) │
└────┬─────────────────────┘
     │
     │ 5. Enviado al cliente MCP
     ▼
┌─────────────────────────────┐
│  MultiServerMCPClient       │
│  (encuentra servidor adecuado) │
└────┬────────────────────────┘
     │
     │ 6. Conecta con servidor `StringTools`
     ▼
┌────────────────────────────┐
│  MCP Server (StringTools) │
└────┬──────────────────────┘
     │
     │ 7. Ejecuta: count_words("...")
     ▼
┌──────────────────┐
│ Resultado: 5     │
└────┬─────────────┘
     │
     │ 8. Devuelve resultado al agente
     ▼
┌──────────────────┐
│   LangGraph Agent│
└────┬─────────────┘
     │
     │ 9. Genera respuesta final usando output
     ▼
┌────────────┐
│  Usuario   │
└────────────┘
