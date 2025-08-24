import os
import importlib
import sys
from pathlib import Path

current_dir = Path(__file__).parent

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

EXCLUDE_FILES = ['__init__.py', '__pycache__']

# Enable Windows color support
if sys.platform == 'win32':
    os.system('color')

# Check if llama-cpp-python is available for GGUF functionality
GGUF_AVAILABLE = False
try:
    import llama_cpp
    GGUF_AVAILABLE = True
except ImportError:
    # Use Windows color codes for better visibility
    print("\n" + "=" * 80)
    print("\033[91mWARNING: llama-cpp-python library not found, GGUF functionality is not available\033[0m")
    print("\033[93mTo use GGUF features, install additional dependencies:\033[0m")
    print("\033[96mpip install llama-cpp-python\033[0m")
    
    # Check if installation guide exists and provide link
    install_guide = current_dir / "llama_cpp_install.md"
    if install_guide.exists():
        print("\033[93mFor detailed installation instructions with CUDA support, please see:\033[0m")
        print(f"\033[96m{install_guide}\033[0m")
    
    print("\033[92mBasic MiniCPM functionality is still available\033[0m")
    print("=" * 80 + "\n")
except Exception as e:
    print("\n" + "=" * 80)
    print(f"\033[91mError loading GGUF dependencies: {str(e)}\033[0m")
    print("\033[92mBasic MiniCPM functionality is still available\033[0m")
    print("=" * 80 + "\n")

# Process all Python files in the directory (auto-registration functionality)
for file in current_dir.glob('*.py'):
    if file.name not in EXCLUDE_FILES:
        try:
            module_name = file.stem
            spec = importlib.util.spec_from_file_location(module_name, str(file))
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            
            # Skip GGUF module if llama-cpp-python is not available
            if not GGUF_AVAILABLE and 'GGUF' in module_name:
                print(f"\033[93mSkipping {module_name} - GGUF functionality not available\033[0m")
                continue
                
            spec.loader.exec_module(module)
            
            if hasattr(module, 'NODE_CLASS_MAPPINGS'):
                NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
                print(f"\033[92mLoaded {module_name} nodes: {list(module.NODE_CLASS_MAPPINGS.keys())}\033[0m")
            
            if hasattr(module, 'NODE_DISPLAY_NAME_MAPPINGS'):
                NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
                
        except Exception as e:
            print(f"\033[91mError loading module {module_name}: {str(e)}\033[0m")
            if 'GGUF' not in module_name:  # Only show warning for non-GGUF modules
                print(f"\033[93mWarning: Failed to load {module_name} module\033[0m")

print(f"\n\033[92mMiniCPM nodes loaded: {list(NODE_CLASS_MAPPINGS.keys())}\033[0m")
print(f"\033[92mTotal nodes registered: {len(NODE_CLASS_MAPPINGS)}\033[0m")

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
