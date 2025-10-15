import os 
import bcrypt


#finds the output files in the current directory
def list_output_files():
    files = [f for f in os.listdir() if f.startswith("output") and f.endswith(".txt")]
    return sorted(files)


def choose_file(files):
    if not files:
        print("No output files found.")
        return None
    
    # shows available files to hash (exclude already hashed files)
    files = [f for f in files if not f.endswith("_hashed.txt")]
    print("Available output files:")
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")

    #prompts user to choose a file
    while True:
        choice = input("Enter file number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            return files[int(choice) - 1]
        print("Invalid choice. Try again.")

def hash_passwords_in_file(filename):
    #reads passwords from the chosen file
    output_file = filename.replace(".txt", "_hashed.txt")

    with open(filename, 'r', encoding="utf-8") as fin, open(output_file, 'w', encoding="utf-8") as fout:

        for line in fin:
            pwd = line.strip()
            if not pwd: 
                continue

            salt = bcrypt.gensalt(rounds=12)  # rounds=12 is secure & balanced
            hashed = bcrypt.hashpw(pwd.encode("utf-8"), salt)

            # store as UTF-8 string
            fout.write(hashed.decode("utf-8") + "\n")

    print(f"Hashed passwords written to {output_file}")


if __name__ == "__main__":
    files = list_output_files()
    chosen = choose_file(files)
    if chosen:
        hash_passwords_in_file(chosen)

