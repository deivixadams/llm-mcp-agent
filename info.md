# LangGraph + MCP + Ollama = Plug-n-play AI agents with real-world utility

## Git
git add . && git commit -m "🚀 Actualización: README completo, licencia con atribución y funcionalidad final MCP" && git push origin main


## Git
git add . && git commit -m "🚀 Muestra los tools de forma adecuada!" && git push origin main



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


# Comandos

Read the file "./sandbox/hola.txt"
What files are in the "./sandbox" directory?
Write "Pensamiento Aumentado" to a file named "./sandbox/idea.txt"
What does the file "./sandbox/idea.txt" say?
Overwrite "./sandbox/idea.txt" with "Nueva idea brillante para el curso de IA"