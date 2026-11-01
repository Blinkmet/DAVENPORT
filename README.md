# Password Checker

Asks the user to type a password and rates its strength.

## What it does

- Prompts for a password with `Type a password:`
- Rejects any password on a built-in blocklist of the 20 most common passwords, regardless of its score
- Otherwise rates it:
  - `Weak` (0-1 points)
  - `Fair` (2 points)
  - `Strong` (3 points)
  - `Excellent` (4 points)

Scoring, 1 point each for:

1. Length of at least 8 characters
2. Mix of uppercase and lowercase letters
3. Contains a digit
4. Contains a symbol (non-alphanumeric character)

Common passwords return `Rejected` from `rate_password()`, and the program prints a rejection message instead of a strength rating.

## How to run

```sh
python3 password_check.py
```

Then type a password when prompted.

Example:

```sh
$ python3 password_check.py
Type a password: P@ssw0rd123
Password strength: Excellent
```

Rejected example:

```sh
$ python3 password_check.py
Type a password: Password123!
Password rejected: too common, choose another password.
```
