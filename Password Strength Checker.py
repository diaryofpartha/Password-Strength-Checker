import re
print("*" * 60)

def check_password_complexity(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.match(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?]', password))

    # Check criteria and provide feedback
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong password! Well done."
    else:
        feedback = "Weak password. Consider:"
        if not length_criteria:
            feedback += "\n- Length should be at least 8 characters."
        if not uppercase_criteria:
            feedback += "\n- Include at least one uppercase letter."
        if not lowercase_criteria:
            feedback += "\n- Include at least one lowercase letter."
        if not digit_criteria:
            feedback += "\n- Include at least one digit."
        if not special_char_criteria:
            feedback += "\n- Include at least one special character (!@#$%^&*()_+-=[]{};\\':|,.<>/?)."

        return feedback

while True:
    option = input("Enter 'n' for a new password or 'q' to quit: ")
    if option.lower() == 'n':
        while True:
            password = input("Enter your password: ")
            feedback = check_password_complexity(password)
            print(feedback)
            print("\n-----------------------------------------")
            if "Strong" in feedback:
                break
            else:
                print("Enter a strong password:")
                password = input("Try Again: ")
                feedback = check_password_complexity(password)
                print(feedback)
                print("\n-----------------------------------------")
                if "Strong" in feedback:
                    option = input("Enter 'n' for a new password or 'q' to quit: ")
                    break
    elif option.lower() == 'q':
        print("Exiting...")
        print("\n----------------------------------------------")
        break
    else:
        print("Invalid option. Please enter 'n' or 'q'.")