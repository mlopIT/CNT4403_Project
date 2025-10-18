import os
import hashlib
import tkinter as tk
from tkinter import filedialog
import sys

# ------- CORE LOGIC -------

def generate_unique_filename(base_name="sha512hash_raw.txt"):
    """
    Generates a unique filename by appending a number if the file already exists.
    e.g., sha512hash_raw.txt, sha512hash_raw1.txt, sha512hash_raw2.txt, etc.
    """
    if not os.path.exists(base_name):
        return base_name

    # Separate base name and extension
    base, ext = os.path.splitext(base_name)
    
    counter = 1
    while True:
        # Create the new filename with the counter
        new_filename = f"{base}{counter}{ext}"
        
        # Check if this new filename exists
        if not os.path.exists(new_filename):
            return new_filename
        
        counter += 1

def hash_passwords_in_file_sha512_raw(filename):
    """
    Reads passwords from a file and hashes them using RAW SHA-512 
    (no salting or key stretching) and writes the hash to a unique output file 
    with each hash on a new line.
    
    """
    try:
        # Determine the unique output filename
        output_file = generate_unique_filename(base_name="sha512hash_raw.txt")

        print(f"\nProcessing passwords from: {filename}...")
        
        # A list to hold all the generated raw hashes
        all_raw_hashes = []
        passwords_hashed = 0

        with open(filename, 'r', encoding="utf-8") as fin:
            for line in fin:
                pwd = line.strip()
                if not pwd: 
                    continue
                
                # Create the SHA-512 hash object
                hasher = hashlib.sha512()
                
                # Hash ONLY the password bytes (raw hash)
                hasher.update(pwd.encode("utf-8"))
                
                # Get the final hash in hexadecimal string format
                hashed_pwd = hasher.hexdigest()

                # Store the hash
                all_raw_hashes.append(hashed_pwd)
                passwords_hashed += 1

        # Check if we actually hashed anything
        if not all_raw_hashes:
            print("No valid passwords found to hash. Output file not created.")
            return

        # Ensure the directory exists for the output file
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
        
        # Write all the raw hashes at once
        with open(output_file, 'w', encoding="utf-8") as fout:
            fout.write('\n'.join(all_raw_hashes))


        print(f"Success: Hashed {passwords_hashed} passwords.")
        print(f"Hashed passwords (raw SHA-512) written to: {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred during hashing: {e}")


# ------- USER INTERFACE -------

def introductory_prompt():
    """Prints a welcome statement and asks the user for input to continue."""
    print("==================================================================")
    print("      Password File Hasher (using RAW SHA-512)")
    print("------------------------------------------------------------------")
    print("This program will open a file dialog, allowing you to select a ")
    print("text file containing passwords (one password per line).")
    print("It will then hash the passwords using the raw SHA-512 algorithm.")
    print("==================================================================")
    
    input("Press Enter or any key to open the file selection window...")
    print("\nOpening file dialog...")


def choose_file_with_dialog():
    """
    Opens a native file selection dialog and returns the chosen file path.
    Ensures the dialog gets focus on Windows/in IDEs.
    """
    try:
        root = tk.Tk()
        root.withdraw() 
        
        # Force the root window to the top so the filedialog gets focus
        root.attributes("-topmost", True) 

        # Open the file selection dialog
        file_path = filedialog.askopenfilename(
            title="Select a text file to hash",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        
        # After the dialog closes, turn off topmost and destroy the root
        root.attributes("-topmost", False)
        root.destroy()
        
        return file_path
    
    except Exception as e:
        print(f"An error occurred while opening the file dialog: {e}")
        sys.exit(1) 


# ------- MAIN EXECUTION -------

if __name__ == "__main__":
    
    introductory_prompt()
    
    chosen_file_path = choose_file_with_dialog()

    if chosen_file_path:
        hash_passwords_in_file_sha512_raw(chosen_file_path) 
    else:
        print("\nFile selection cancelled. Program exiting.")