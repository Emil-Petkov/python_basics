def password_guess(guess: str):
    correct_password = 's3cr3t!P@ssw0rd'

    if not guess == correct_password:
        return 'Wrong password!'

    else:
        return 'Welcome'


guess_password = input()
print(password_guess(guess_password))
