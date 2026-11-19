username = input("Enter your username: ")
password = input("Enter your password: ")

print("\nPASSWORD VALIDATION REPORT")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

has_length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

print("\nValidation Rules")
print(f"[{'PASS' if has_length else 'FAIL'}] Minimum 8 characters ({len(password)} characters)")
print(f"[{'PASS' if has_digit else 'FAIL'}] At least one digit")
print(f"[{'PASS' if has_upper else 'FAIL'}] At least one uppercase letter")

print("\nResult")
if has_length and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID")
