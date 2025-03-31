# src/sibling_directory/sibling_module.py
from src.child_directory.child_module import child_function  # Absolute import

print(f"🔄 Importing {__name__}")

def sibling_function():
    print("🟡 Sibling Module Function Called!")
    child_function()
