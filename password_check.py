COMMON_PASSWORDS = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "12345678",
    "12345",
    "1234567",
    "1234567890",
    "letmein",
    "welcome",
    "admin",
    "abc123",
    "password1",
    "123123",
    "qwerty123",
    "1q2w3e4r",
    "111111",
    "123qwe",
    "Password123!",
    "P@ssw0rd",
]

_COMMON_PASSWORDS_LOWER = frozenset(p.lower() for p in COMMON_PASSWORDS)


def is_common_password(password: str) -> bool:
    """Check if a password is on the common-password blocklist (case-insensitive)."""
    return password.lower() in _COMMON_PASSWORDS_LOWER


def rate_password(password: str) -> str:
    """Rate a password as Weak, Fair, Strong, Excellent, or Rejected.

    Returns "Rejected" for any password on the COMMON_PASSWORDS list,
    no matter how it would otherwise score.

    Otherwise scores one point for each of:
    1. Length of at least 8 characters
    2. Mix of uppercase and lowercase letters
    3. Contains a digit
    4. Contains a symbol (non-alphanumeric character)
    """
    if is_common_password(password):
        return "Rejected"

    score = 0

    if len(password) >= 8:
        score += 1

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    if has_lower and has_upper:
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Fair"
    elif score == 3:
        return "Strong"
    else:
        return "Excellent"


def main():
    password = input("Type a password: ")
    rating = rate_password(password)
    if rating == "Rejected":
        print("Password rejected: too common, choose another password.")
    else:
        print(f"Password strength: {rating}")


if __name__ == "__main__":
    main()
