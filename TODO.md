# Project To Do List

## Features
- [x] Implement the password generation core logic for the pwd_generator python file.
- [ ] Add a limit to how many passwords you can save to output file in multi_pwgen_v5.py
- [ ] Develop a python script that can hash plaintext lists/files containing passwords into unreadable hash strings using algorithms like (bcrypt, PBKDF2, SHA512 crypt)
- [ ] Generate password datasets (usernames + plaintext) and hash them locally with common hash algorithms (bcrypt, PBKDF2, SHA512 crypt) to emulate how they're stored. 
- [ ] Password policy definition (what to emulate) Create multiple policy “buckets” to compare. Example policies: - Policy A (weak): min 8 chars, no other enforcement. - Policy B (lowercase + uppercase required): min 8 chars, must include at least one uppercase, one lowercase. - Policy C (+numbers): B + at least one digit. - Policy D (+special): C + at least one special character. - Policy E (length emphasis): min 12 chars, no composition requirement. - Policy F (complex but memorable): passphrase style (4 random words, optional separator and digit).
