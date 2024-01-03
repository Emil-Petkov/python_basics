def password_guess(user_input: str):
    correct_password = 's3cr3t!P@ssw0rd'

    if user_input == correct_password:
        return 'Welcome'

    return 'Wrong password!'


user_input = input()
print(password_guess(user_input))
