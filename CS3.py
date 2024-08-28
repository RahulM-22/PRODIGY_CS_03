import re

def calculate_strength(password):
    # Initialize strength variables
    length_score = 0
    case_score = 0
    digit_score = 0
    special_score = 0

    # Check length
    if len(password) >= 8:
        length_score = 1
    if len(password) >= 12:
        length_score = 2
    if len(password) >= 16:
        length_score = 3

    # Check for uppercase and lowercase
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        case_score = 2
    elif re.search(r'[a-zA-Z]', password):
        case_score = 1

    # Check for digits
    if re.search(r'[0-9]', password):
        digit_score = 2
        if len(re.findall(r'[0-9]', password)) > 2:
            digit_score = 3

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        special_score = 2
        if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) > 1:
            special_score = 3

    # Calculate total score
    total_score = length_score + case_score + digit_score + special_score

    return total_score

def password_feedback(total_score):
    if total_score <= 3:
        return "Weak"
    elif total_score <= 6:
        return "Moderate"
    elif total_score <= 8:
        return "Strong"
    else:
        return "Very Strong"

def main():
    print("Password Strength Checker")

    while True:
        password = input("Enter a password to check (or 'exit' to quit): ")

        if password.lower() == 'exit':
            break

        score = calculate_strength(password)
        feedback = password_feedback(score)

        print(f"Password strength: {feedback}")

        if feedback == "Weak":
            print("Try to make your password longer, include both upper and lower case letters, numbers, and special characters.")
        elif feedback == "Moderate":
            print("Consider adding more variety such as numbers, special characters, or making it longer.")
        elif feedback == "Strong":
            print("Your password is strong but you can still add more diversity for extra security.")
        elif feedback == "Very Strong":
            print("Your password is very strong.")

        print()  # Blank line for readability

if __name__ == "__main__":
    main()
