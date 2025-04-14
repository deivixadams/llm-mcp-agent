from langchain_ollama import ChatOllama

def load_model(model_name: str = "llama3.2"):
    """
    Carga un modelo de Ollama compatible con LangChain.

    Args:
        model_name (str): Nombre del modelo en Ollama (ej. 'llama3.2').

    Returns:
        ChatOllama: Modelo listo para ser usado con agentes.
    """
    return ChatOllama(model=model_name)
