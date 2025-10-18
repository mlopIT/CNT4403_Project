import os
import tkinter as tk
from tkinter import filedialog
import sys

# ------- CORE LOGIC -------

def count_file_lines(filename):
    """
    Reads a file and counts the number of lines.
    """
    try:
        line_count = 0
        
        print(f"\nProcessing file: {filename}...")
        
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
        
        print(f"Success: The file has {line_count} lines.")
        
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except UnicodeDecodeError:
        print(f"Error: Could not read file '{filename}' with UTF-8 encoding. It might be a binary file.")
    except Exception as e:
        print(f"An unexpected error occurred while processing the file: {e}")

# ------- USER INTERFACE -------

def introductory_prompt():
    """Prints a welcome statement and asks the user for input to continue."""
    print("==================================================================")
    print("           File Line Counter Tool")
    print("------------------------------------------------------------------")
    print("This program will open a file dialog, allowing you to select any ")
    print("text file. It will then count and display the total number of lines.")
    print("==================================================================")
    
    input("Press Enter or any key to open the file selection window...")
    print("\nOpening file dialog...")


def choose_file_with_dialog():
    """
    Opens a native file selection dialog and returns the chosen file path.
    Ensures the dialog gets focus.
    """
    try:
        # Initialize Tkinter
        root = tk.Tk()
        root.withdraw() 
        
        # Force the root window to the top so the filedialog gets focus
        root.attributes("-topmost", True) 

        # Open the file selection dialog
        file_path = filedialog.askopenfilename(
            title="Select a text file to count lines from",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        
        # After the dialog closes, turn off topmost and destroy the root
        root.attributes("-topmost", False)
        root.destroy()
        
        return file_path
    
    except Exception as e:
        print(f"An error occurred while opening the file dialog: {e}")
        # Return an empty string if the dialog fails
        return ""


# ------- MAIN EXECUTION -------

if __name__ == "__main__":
    
    introductory_prompt()
    
    chosen_file_path = choose_file_with_dialog()

    if chosen_file_path:
        # Check if the path is a file (not strictly necessary but good practice)
        if os.path.isfile(chosen_file_path):
            count_file_lines(chosen_file_path)
        else:
            # This handles the case where a user cancels the file dialog
            print("\nFile selection was cancelled or an invalid path was returned.")
    else:
        print("\nFile selection cancelled. Program exiting.")