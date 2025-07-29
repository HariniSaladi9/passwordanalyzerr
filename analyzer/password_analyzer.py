from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    return {
        "score": result['score'],
        "guesses": result['guesses'],
        "feedback": result['feedback'],
    }
