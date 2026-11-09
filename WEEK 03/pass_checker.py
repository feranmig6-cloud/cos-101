# Classify a valid score using a pass mark of 50.

score = float(input("Enter your score: "))


if score >= 50:
    print("Result:You Passed")
else:
    print("Result:You Failed")


score = 75

print(score >= 0 and score <= 100)


score = 120

print(score < 0 or score > 100)



score = float(input("Enter a score from 0 to 100: "))

if 0 <= score <= 100:
    print("The score is within the valid range.")
else:
    print("Invalid score.")


