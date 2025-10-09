# CNT4403_Project


## Overview
The **`multi-pwgen-v4.py`** script is a utility that batch-generates multiple passwords using a separate core password generation script (**`pwd_generator_v4.py`**) and safely stores all generated passwords in a single output file.  

It ensures that no existing output files are ever overwritten by automatically appending a number to the filename (e.g., `output1.txt`, `output2.txt`) if `output.txt` already exists in the same directory. The output file is always saved in the same folder as the script itself.

---

## Prerequisites
- A separate password generator script named **`pwd_generator_v4.py`** must exist in the same directory as **`multi-pwgen-v4.py`**.  
- The `pwd_generator_v4.py` script must print passwords using the standard `print()` function, as **`multi-pwgen-v4.py`** captures its output via stream redirection.  
- No external dependencies are required — only Python’s standard library.

---

## Installation and Usage

### 1. Project Setup
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/mlopIT/CNT4403_Project/
cd CNT4403_Project
```

Add your password generator script:
- Ensure your password generation script is saved as **`pwd_generator_v4.py`** inside the project directory.

---

### 2. Execution
Run the main runner script from your terminal:
```bash
python multi-pwgen-v4.py
```

When prompted, enter the number of passwords you wish to generate:
```
Enter the number of passwords you would like to create: 50
```

---

### 3. Output
After generation completes, the script displays confirmation and the full path to the saved file:
```
Successfully generated 50 passwords and saved the complete output.
----------------------------------------
File Saved As: output.txt
Location:
    /path/to/your/project/CNT4403_Project/output.txt
----------------------------------------
```

If `output.txt` already exists, the program automatically saves to `output1.txt`, `output2.txt`, and so on.

---

## Project Files

| File | Description |
|------|--------------|
| `multi-pwgen-v4.py` | Main runner script. Handles input, runs the password generator multiple times, captures output, and saves results to a uniquely named file in the same directory. |
| `pwd_generator_v4.py` | **(Required)** Core password generation logic provided by the user. Must output passwords using `print()`. |
| `requirements.txt` | Lists required Python packages (only standard library modules are used). |

---

## Example Workflow
1. Place both scripts in the same directory.  
2. Run `multi-pwgen-v4.py`.  
3. Enter how many passwords you need.  
4. Find your results saved automatically in `output.txt` or a numbered variant.  

---

## License
This project is for educational and demonstration purposes as part of **CNT4403 - Computing and Network Security** coursework.