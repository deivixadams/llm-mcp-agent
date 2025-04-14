# mcp_core/secure_path.py

import os

SANDBOX_ROOT = os.path.abspath("sandbox")

def secure_path(path: str) -> str:
    """
    Resuelve una ruta asegurándose de que esté dentro del sandbox.
    Si la ruta es relativa, la convierte en absoluta dentro del sandbox.
    """
    # Si ya comienza con 'sandbox/' o './sandbox/', no tocar
    if os.path.abspath(path).startswith(SANDBOX_ROOT):
        return path

    # Prepend sandbox
    full_path = os.path.abspath(os.path.join("sandbox", path))

    # Validar que no escapa por ../
    if not full_path.startswith(SANDBOX_ROOT):
        raise ValueError(f"Access denied: {path} is outside the sandbox.")
    
    return full_path
