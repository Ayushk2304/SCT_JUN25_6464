import re

def check_password_strength(password):
    score = 0
    remarks = ""

    # Criteria checks
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Scoring
    if not length_error:
        score += 1
    if not digit_error:
        score += 1
    if not uppercase_error:
        score += 1
    if not lowercase_error:
        score += 1
    if not symbol_error:
        score += 1

    # Result based on score
    if score == 5:
        remarks = "Very Strong 💪"
    elif score == 4:
        remarks = "Strong 👍"
    elif score == 3:
        remarks = "Medium 🤔"
    elif score == 2:
        remarks = "Weak 👎"
    else:
        remarks = "Very Weak ❌"

    print(f"\nPassword: {password}")
    print(f"Strength Score: {score}/5")
    print(f"Result: {remarks}")

    # Optional detailed feedback
    print("\nFeedback:")
    if length_error:
        print("❌ Password should be at least 8 characters long.")
    if digit_error:
        print("❌ Include at least one number.")
    if uppercase_error:
        print("❌ Include at least one uppercase letter.")
    if lowercase_error:
        print("❌ Include at least one lowercase letter.")
    if symbol_error:
        print("❌ Include at least one special character (!@#$ etc.)")

def main():
    print("=== Password Strength Checker ===")
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)

if __name__ == "__main__":
    main()
