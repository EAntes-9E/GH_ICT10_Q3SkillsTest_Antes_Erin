from pyscript import display, document


def check(event):
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    result = document.getElementById("result")

    # Check username
    if len(username) < 7:
        result.innerHTML = "Username must be at least 7 characters"
        return

    # Check password
    if len(password) < 10:
        result.innerHTML = "Password must be at least 10 characters"
        return

    if not any(letter.isalpha() for letter in password):
        result.innerHTML = "Password must have a letter"
        return

    if not any(number.isdigit() for number in password):
        result.innerHTML = "Password must have a number"
        return

    result.innerHTML = "Account Created!"