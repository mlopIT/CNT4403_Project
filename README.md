# CNT4403_Project

## Overview
The **`multi-pwgen-v5.py`** script is a utility that generates multiple passwords using a separate core password generation script (**`pwd_generator_v4.py`**) and safely stores all generated passwords in a single output file.

Additionally, the **`pwd_generator_v4.py`** script creates the password that the **`multi-pwgen-v5.py`** script uses. More specifically, it generates a password with a length randomly anywhere between 8 and 12. It uses capital and lowercase letters, as well as digits and special characters. But the script only uses the Exclamation mark (!) and the At sign (@) characters because these are the universally allowed special characters when users create passwords for logging into an online service. And because most users only use 2 numbers and 2 special characters when creating passwords, the **`pwd_generator_v4.py`** script will only generate passwords with those amounts, but of course, you can always change and set the amount you prefer.

It ensures that no existing output files are ever overwritten by automatically appending a number to the filename (e.g., `output1.txt`, `output2.txt`) if `output.txt` already exists in the same directory. The output file is always saved in the same folder as the script itself.

---

## Prerequisites
- A separate password generator script named **`pwd_generator_v4.py`** must exist in the same directory as **`multi-pwgen-v5.py`**.  
- The `pwd_generator_v4.py` script must print passwords using the standard `print()` function, as **`multi-pwgen-v5.py`** captures its output via stream redirection.  
- No external dependencies are required — only Python’s standard library.

---

## Installation and Usage

Note: You do not have to follow the steps below, if you want to use the python files in an IDE of your choice. The steps below apply if you want to use the Command Terminal in Windows.

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

### 3. Output
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
| `requirements.txt` | Lists required Python packages (only standard library modules are used). |

---

## Example Workflow
1. Place both scripts in the same directory.  
2. Run `multi-pwgen-v5.py`.  
3. Enter how many passwords you need.  
4. Find your results saved automatically in `output.txt` or a numbered variant.  

---

## License
This project is for educational and demonstration purposes as part of **CNT4403 - Computing and Network Security** coursework.