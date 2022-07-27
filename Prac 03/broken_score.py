try:
    score = float(input("Enter score: "))
    if 90 > score >= 50:
        print("Passable")
    if score >= 90:
        print("Excellent")
    if score < 50:
        print("Bad")
except ValueError:
    print("Invalid score")