import sys
import os
import importlib

# Forza la policy per Windows PRIMA di qualsiasi import di Rasa
if sys.platform == "win32":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Ora importa e avvia Rasa
if __name__ == "__main__":
    importlib.import_module("rasa.__main__").main()