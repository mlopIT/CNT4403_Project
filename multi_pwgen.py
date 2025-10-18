import sys
import io
import os

# Constants for the New Check
MAX_OUTPUT_COUNT = 100
BASE_NAME = 'output'
EXTENSION = '.txt'

# Get the directory where this script is located.
# This ensures output.txt is always saved next to the Python file.
# Note: In some execution environments (like notebooks), __file__ might not be defined.
# We'll use os.path.dirname(os.path.abspath(__file__)) if possible, or fall back to '.'
try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # Fallback directory if __file__ is not available (e.g., running in an interactive session)
    SCRIPT_DIR = os.getcwd() 

# Helper Function for Unique Filenames
def get_unique_filename(base_name=BASE_NAME, extension=EXTENSION):
    """
    Checks if a file exists in the SCRIPT_DIR and returns a unique, numbered filename.
    
    If 'output.txt' exists, it tries 'output1.txt', then 'output2.txt', etc.
    The filename returned includes the full path to the script's directory.
    
    *** MODIFICATION: Checks for the existence of the 100th file and exits if found. ***
    """
    
    # Check for the MAX_OUTPUT_COUNT file (e.g., 'output100.txt')
    # If it exists, we stop the program.
    max_filepath = os.path.join(SCRIPT_DIR, f"{base_name}{MAX_OUTPUT_COUNT}{extension}")
    if os.path.exists(max_filepath):
        print(f"\nMaximum file limit reached!")
        print(f"The file '{os.path.basename(max_filepath)}' already exists.")
        print("Program is exiting to prevent further file generation.")
        sys.exit(1) # Exit with a non-zero status indicating an error/intentional stop

    # Start checking with the base name (e.g., '/path/to/script/output.txt')
    filepath_base = os.path.join(SCRIPT_DIR, f"{base_name}{extension}")
    
    if not os.path.exists(filepath_base):
        return filepath_base

    # If the base name exists, start checking numbered versions
    counter = 1
    # The loop will not reach MAX_OUTPUT_COUNT because the check above handles it.
    while True:
        # Create the full path with the counter (e.g., '/path/to/script/output1.txt')
        filepath = os.path.join(SCRIPT_DIR, f"{base_name}{counter}{extension}")
        if not os.path.exists(filepath):
            return filepath
        counter += 1

# Check the file limit IMMEDIATELY before asking for user input.
try:
    # Just call the function to run the check logic. If output100.txt exists, it will sys.exit(1).
    # We discard the returned path because we'll generate it again later.
    _ = get_unique_filename(base_name=BASE_NAME, extension=EXTENSION)
except SystemExit:
    # Re-raise the SystemExit to stop the program immediately.
    # This is only necessary if your environment suppresses the exit call. 
    # In most console environments, the call inside get_unique_filename is enough.
    raise
except Exception as e:
    # Handle unexpected errors during the check
    print(f"An unexpected error occurred during the file limit check: {e}")
    sys.exit(1)

# Get the number of passwords the user wants to generate.
while True:
    try:
        num_times = int(input("Enter the number of passwords you would like to create: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Preserve the original stdout and redirect it to a StringIO buffer.
# All 'print()' statements from the executed script will now write to this buffer.
old_stdout = sys.stdout
stdout_capture = io.StringIO()
sys.stdout = stdout_capture

try:
    # Execute the password generation script multiple times.
    # We join the script's directory with the filename to ensure we find 'pwd_generator_v4.py' 
    # even if we are not running from the script's directory.
    pwd_script_path = os.path.join(SCRIPT_DIR, 'pwd_generator_v4.py')
    script_content = open(pwd_script_path).read()

    for i in range(num_times):
        # Execute the code. Its output is captured in stdout_capture.
        exec(script_content)

except FileNotFoundError:
    # Important error handling: the script dependency must exist.
    print(f"\nError: The required script 'pwd_generator_v4.py' was not found.")
    print(f"Looked for file at: {pwd_script_path}")
    print("Please ensure it is in the same directory as this file.")

finally:
    # ALWAYS restore the original stdout immediately.
    sys.stdout = old_stdout

# Get the full captured content from the buffer.
captured_output = stdout_capture.getvalue()
captured_output_cleaned = captured_output.rstrip() # removes any trailing whitespace like final newline

# Determine the unique output filename (this now returns the full path)
output_filename_with_path = get_unique_filename(base_name=BASE_NAME, extension=EXTENSION)
display_filename = os.path.basename(output_filename_with_path) # Name only for display

# Write the entire captured output to the unique file once.
if captured_output_cleaned: # Only write if there is content (e.g., if no FileNotFoundError occurred)
    try:
        # Use the newly determined unique filename (which includes the full path) here
        with open(output_filename_with_path, 'w') as f:
            f.write(captured_output_cleaned)

        # The full path is already in output_filename_with_path
        full_path = output_filename_with_path

        print(f"\nSuccessfully generated {num_times} passwords and saved the complete output.")
        print("-" * 40)
        print(f"File Saved As: {display_filename}")
        print(f"Location:")
        print(f"\t{full_path}")
        print("-" * 40)
    except Exception as e:
        print(f"\nAn unexpected error occurred while writing to '{display_filename}': {e}")