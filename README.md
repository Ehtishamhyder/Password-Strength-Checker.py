# Password Strength Checker (Python)

##  About This Project

This is a simple Password Strength Checker built using Python.  
The program checks how strong a password is based on different conditions like:

- Length of the password  
- Sequential numeric patterns (like 1234 or 4321)  
- Use of uppercase and lowercase letters  
- Use of digits  
- Use of special characters <img width="1468" height="110" alt="Screenshot (787)" src="https://github.com/user-attachments/assets/e0984aa5-a258-449c-a913-2c1208cf7082" />
<img width="1468" height="110" alt="Screenshot (787)" src="https://github.com/user-attachments/assets/e0984aa5-a258-449c-a913-2c1208cf7082" />
<img width="1403" height="105" alt="Screenshot (660)" src="https://github.com/user-attachments/assets/df287072-22f7-4c2f-b46d-c74ced458706" />
<img width="1403" height="105" alt="Screenshot (660)" src="https://github.com/user-attachments/assets/df287072-22f7-4c2f-b46d-c74ced458706" />


---

##  How It Works

1. The program asks the user to enter a password.
2. It first checks if the password is a sequential numeric pattern.
3. If not sequential, it checks:
   - Password length
   - Character combinations
4. Finally, it displays the strength percentage and category.

```bash
python password_checker.py
