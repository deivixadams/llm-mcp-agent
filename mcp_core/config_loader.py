import json
from typing import Dict


def load_server_config(config_path: str) -> Dict[str, dict]:
    """
    Carga el archivo de configuración MCP (formato JSON).

    Args:
        config_path (str): Ruta al archivo server_config.json

    Returns:
        Dict[str, dict]: Diccionario con la configuración de los servidores
    """
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            servers = data.get("mcpServers", {})

            if not servers:
                raise ValueError("El archivo de configuración no contiene servidores MCP válidos.")

            return servers

    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {config_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error al parsear el JSON: {e}")
