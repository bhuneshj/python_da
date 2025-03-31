# src/main.py
import sys
from src.child_directory.child_module import child_function
from src.sibling_directory.sibling_module import sibling_function

print(f"🚀 Running {__name__}")

if __name__ == "__main__":
    #child_function()  # Call once from main
    sibling_function()  # This also calls child_function(), so we should expect one extra call
