import sys
import io
import os
import tkinter as tk
from tkinter import filedialog

# Constants for the New Check
MAX_OUTPUT_COUNT = 100
BASE_NAME = 'output'
EXTENSION = '.txt'

# ------- Directory and Filename Logic -------

# Get the directory where this script is located.
try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # Fallback directory if __file__ is not available
    SCRIPT_DIR = os.getcwd() 

def get_unique_filename(base_name=BASE_NAME, extension=EXTENSION):
    """
    Checks the file limit and returns a unique, numbered filename (full path).
    Exits the program if the maximum file limit is reached.
    """
    
    # Check for the MAX_OUTPUT_COUNT file (e.g., 'output100.txt')
    max_filepath = os.path.join(SCRIPT_DIR, f"{base_name}{MAX_OUTPUT_COUNT}{extension}")
    if os.path.exists(max_filepath):
        print(f"\nMaximum file limit reached!")
        print(f"The file '{os.path.basename(max_filepath)}' already exists.")
        print("Program is exiting to prevent further file generation.")
        sys.exit(1)

    # Find the next available filename
    filepath_base = os.path.join(SCRIPT_DIR, f"{base_name}{extension}")
    
    if not os.path.exists(filepath_base):
        return filepath_base

    counter = 1
    while True:
        filepath = os.path.join(SCRIPT_DIR, f"{base_name}{counter}{extension}")
        if not os.path.exists(filepath):
            return filepath
        counter += 1

# ------- User Interface Functions -------

def introductory_prompt():
    """Prints a welcome statement and asks the user for input to continue."""
    print("==================================================================")
    print("       Multi-Script Executor & Output Saver")
    print("------------------------------------------------------------------")
    print("This program will:")
    print("Prompt you to select a Python script (*.py) to execute.")
    print("Ask how many times to execute the selected script.")
    print("Capture ALL 'print()' output from the executions.")
    print("Save the combined output to a new, unique 'outputN.txt' file.")
    print("==================================================================")
    
    input("Press Enter or any key to select the script to execute...")
    print("\nOpening file dialog...")

def choose_script_with_dialog():
    """Opens a native file selection dialog for a Python script."""
    try:
        root = tk.Tk()
        root.withdraw() 
        
        # Force the root window to the top so the filedialog gets focus
        root.attributes("-topmost", True) 

        # Open the file selection dialog, filtered for Python files
        script_path = filedialog.askopenfilename(
            title="Select a Python script (*.py) to execute",
            initialdir=SCRIPT_DIR, # Start in the current directory
            filetypes=(("Python Scripts", "*.py"), ("All Files", "*.*"))
        )
        
        # After the dialog closes, turn off topmost and destroy the root
        root.attributes("-topmost", False)
        root.destroy()
        
        return script_path
    
    except Exception as e:
        print(f"An error occurred while opening the file dialog: {e}")
        sys.exit(1)

# ------- Main Execution -------

if __name__ == "__main__":
    
    # Display intro and pause
    introductory_prompt()

    # Check file limit IMMEDIATELY before asking for user input.
    try:
        _ = get_unique_filename(base_name=BASE_NAME, extension=EXTENSION)
    except SystemExit:
        # Stop program if max file count is reached
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during the file limit check: {e}")
        sys.exit(1)
    
    # Get the script path from the user
    script_path_to_execute = choose_script_with_dialog()

    if not script_path_to_execute:
        print("\nScript selection cancelled. Program exiting.")
        sys.exit(0)

    # Get the number of times to execute
    while True:
        try:
            num_times = int(input(f"\nEnter the number of times to execute '{os.path.basename(script_path_to_execute)}': "))
            if num_times < 1:
                 print("Please enter a positive whole number.")
                 continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Redirect stdout and read the selected script content
    old_stdout = sys.stdout
    stdout_capture = io.StringIO()
    sys.stdout = stdout_capture
    script_content = ""

    try:
        with open(script_path_to_execute, 'r') as f:
            script_content = f.read()

        # Execute the script multiple times.
        for i in range(num_times):
            exec(script_content)

    except FileNotFoundError:
        print(f"\nError: The selected script was not found at: {script_path_to_execute}")
        
    except Exception as e:
        print(f"\nAn error occurred during script execution: {e}")

    finally:
        # ALWAYS restore the original stdout immediately.
        sys.stdout = old_stdout

    # Process and save the captured output
    captured_output = stdout_capture.getvalue()
    captured_output_cleaned = captured_output.rstrip()

    if captured_output_cleaned:
        output_filename_with_path = get_unique_filename(base_name=BASE_NAME, extension=EXTENSION)
        display_filename = os.path.basename(output_filename_with_path)

        try:
            with open(output_filename_with_path, 'w', encoding='utf-8') as f:
                f.write(captured_output_cleaned)

            print(f"\nSuccessfully executed the script {num_times} times and saved the complete output.")
            print("-" * 40)
            print(f"File Saved As: {display_filename}")
            print(f"Location:")
            print(f"\t{output_filename_with_path}")
            print("-" * 40)
            
        except Exception as e:
            print(f"\nAn unexpected error occurred while writing to '{display_filename}': {e}")
    else:
        # This handles cases where the script was found but produced no output, or if an error occurred before execution.
        print("\nNo output was captured from the executed script(s). No file was saved.")