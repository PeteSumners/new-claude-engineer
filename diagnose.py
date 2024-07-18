import sys
import os
import platform

print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Operating System:", platform.platform())
print("Current working directory:", os.getcwd())
print("Contents of current directory:")
for item in os.listdir():
    print(f"  - {item}")

print("\nEnvironment variables:")
for key, value in os.environ.items():
    print(f"  {key}: {value}")

try:
    import anthropic
    print("\nanthropic library version:", anthropic.__version__)
except ImportError:
    print("\nanthropic library is not installed")

try:
    import asyncio
    print("asyncio library version:", asyncio.__version__)
except ImportError:
    print("asyncio library is not installed")

print("\nPython path:")
for path in sys.path:
    print(f"  - {path}")