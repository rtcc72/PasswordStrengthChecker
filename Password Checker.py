''' Name: Ryan Campbell
Date: 4/16/2023
Project Name: Password Strength Checker

'''

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/checkPwStrength', methods=['POST'])
def checkPwStrength():
    password = request.form['password']
    strength = 0

    # check length
    if len(password) >= 8:
        strength += 1

    # check complexity
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for char in password):
        strength += 1

    # determine strength level
    if strength == 0:
        level = "very weak"
    elif strength == 1:
        level = "weak"
    elif strength == 2:
        level = "fair"
    elif strength == 3:
        level = "strong"
    else:
        level = "very strong"

    return jsonify({'password_strength': level})


if __name__ == '__main__':
    app.run()