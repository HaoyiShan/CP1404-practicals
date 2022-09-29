import random

def main():
    try:
        score = random_score()
        if 90 > score >= 50:
            return "Passable"
        if score >= 90:
            return "Excellent"
        if score < 50:
            return "Bad"
    except ValueError:
        return "Invalid score"


def random_score():
    score = random.randint(0, 100)
    return score


print(main())
