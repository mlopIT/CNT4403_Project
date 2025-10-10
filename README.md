# CNT4403_Project

## Overview
The **`multi-pwgen-v5.py`** script is a utility that generates multiple passwords using a separate core password generation script (**`pwd_generator_v4.py`**) and safely stores all generated passwords in a single output file.

Additionally, the **`pwd_generator_v4.py`** script generates a password with a length randomly anywhere between 8 and 12. It uses capital and lowercase letters, as well as digits and special characters. But the script only uses the Exclamation mark (!) and the At sign (@) characters because these are the universally allowed special characters when users create passwords for logging into an online service. And because most users only use 2 numbers and 2 special characters when creating passwords, the **`pwd_generator_v4.py`** script will only generate passwords with those amounts, but of course, you can always change and set the amount you prefer.

The **`multi-pwgen-v5.py`** script ensures that no existing output files are ever overwritten by automatically appending a number to the filename (e.g., `output1.txt`, `output2.txt`) if `output.txt` already exists in the same directory. The output file is always saved in the same folder as the script itself.

---

## Prerequisites
- A separate password generator script named **`pwd_generator_v4.py`** must exist in the same directory as **`multi-pwgen-v5.py`**.  
- The `pwd_generator_v4.py` script must print passwords using the standard `print()` function, as **`multi-pwgen-v5.py`** captures its output via stream redirection.  
- Some external dependencies are required besides Python’s standard library (like the **bcrypt** package).

---

## Installation and Usage

Note: You do not have to follow anything past the first step below, if you want to use this project's python files in an IDE of your choice. The steps below will apply if you want to use the Command Terminal in Windows.

### 1. Project Setup
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/mlopIT/CNT4403_Project/
cd CNT4403_Project
```

Add your password generator script:
- Ensure your password generation script is saved as **`pwd_generator_v4.py`** inside the project directory.

---

### 2. (Optional but Recommended) Create and Activate a Virtual Environment
A **virtual environment (venv)** isolates your project’s dependencies from the rest of your system. This prevents version conflicts between packages used in other projects and keeps your setup clean and reproducible. If you need additional help understanding how to setup your virtual environment click [here](https://youtu.be/yG9kmBQAtW4?si=dF8kaSLZFXCaIKBi).

To create and activate a virtual environment in PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

Once activated, you’ll notice your terminal prompt changes to show `(venv)` — meaning the environment is active.

To deactivate the environment later, simply run:
```powershell
deactivate
```

---

### 3. Install the bcrypt Package
The **bcrypt** package is required if you plan to use the hashing utility that secures passwords before storage or comparison.

To install it (while your virtual environment is active), run:
```powershell
(venv) pip install bcrypt
```

Expected output:
```
Collecting bcrypt
  Using cached bcrypt-5.0.0-cp39-abi3-win_amd64.whl.metadata (10 kB)
Using cached bcrypt-5.0.0-cp39-abi3-win_amd64.whl (150 kB)
Installing collected packages: bcrypt
Successfully installed bcrypt-5.0.0
```

Using bcrypt ensures your generated or stored passwords are cryptographically secure and protected against brute-force attacks.

---

### 4. Execution
To quickly open the Command Prompt in Windows 10 or 11: 
- Press the Windows key + R to open the Run dialog box, type cmd, and then press Enter.

Next, locate the folder of wherever you've stored the project and right click, then select the option "Copy As Path" or press Ctrl + Shift + C.

Now that you've the file path you can continue...

In the terminal, type the command cd, and paste the file path you copied earlier, and hit Enter. It should look like this:
```bash
cd "example\your filepath\"
```

Run the main runner script from your terminal:
```bash
python multi-pwgen-v5.py
```

When prompted, enter the number of passwords you wish to generate:
```
Enter the number of passwords you would like to create: 5 <--- your input
```

---

### 5. Output
After generation completes, the script displays confirmation and the full path to the saved file:
```
Successfully generated 5 passwords and saved the complete output.
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
| `multi-pwgen-v5.py` | Main runner script. Handles input, runs the password generator multiple times, captures output, and saves results to a uniquely named file in the same directory. |
| `pwd_generator_v4.py` | **(Required)** Core password generation logic provided by the user. Must output passwords using `print()`. |
| `requirements.txt` | Lists required Python packages (bcrypt should be added here if used). |

---

## Example Workflow
1. Place both scripts in the same directory.  
2. Activate your virtual environment.  
3. Install `bcrypt` if you plan to hash passwords.  
4. Run `multi-pwgen-v5.py`.  
5. Enter how many passwords you need.  
6. Find your results saved automatically in `output.txt` or a numbered variant.  

---

## License
This project is for educational and demonstration purposes as part of **CNT4403 - Computing and Network Security** coursework.
