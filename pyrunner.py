import sys
import os
import subprocess

def run_python_file(file_path):
    """
    Run a Python file using the Python interpreter.
    
    Args:
        file_path (str): Path to the Python file to be executed
    
    Returns:
        int: Return code from the Python process
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return 1
    
    if not file_path.endswith('.py'):
        print(f"Warning: File '{file_path}' doesn't have a .py extension.")
    
    try:
        # Get the current Python interpreter path
        python_executable = sys.executable
        
        # Run the Python file as a subprocess
        result = subprocess.run([python_executable, file_path], capture_output=False)
        
        return result.returncode
    except Exception as e:
        print(f"Error executing '{file_path}': {e}")
        return 1

if __name__ == "__main__":
    # Check if file path is provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python runner.py <path_to_python_file>")
        sys.exit(1)
    
    # Get the file path from command line arguments
    file_path = sys.argv[1]
    
    # Run the Python file
    exit_code = run_python_file(file_path)
    
    # Exit with the same exit code
    sys.exit(exit_code)