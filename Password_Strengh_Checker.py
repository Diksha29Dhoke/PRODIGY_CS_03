#password strength checker
import re

# conditions: min 8 chars, digit, uppercase, lowercase, special characters
def password_strength_checker(password):
    if len(password) < 8:
        return "weak: password must contain at least 8 digit!!"

    if not any(char.isdigit() for char in password):
        return "weak: password must contain a digit!!"
    
    if not any(char.isupper() for char in password):
        return "weak: password must contain an uppercase letter !!"
    
    if not any(char.islower() for char in password):
        return "weak: password must contain a lowercase letter !!"
        
    if not re.search(r'[,.?!;:$%*@^&(){}]', password):
        return "medium: password must contain a special character!"
    
    return "Strong:Your password is secured!"
   
def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        strength = password_strength_checker(password)

        if password.lower() == 'exit':
            print("Thank you for using this tool! Hope We helped you knowing the strength of your password. ")
            break
        result = password_strength_checker(password)
        print()
        print(result)

if __name__ == "__main__":
    password_checker()
