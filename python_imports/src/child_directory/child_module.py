# src/child_directory/child_module.py
import sys
from src.parent_module import parent_function  # Use absolute import

print(f"🔄 Importing {__name__}")

def child_function():
    print("🟢 Child Module Function Called!")
    parent_function()
