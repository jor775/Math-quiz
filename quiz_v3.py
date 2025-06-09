import random

# Greet the user
print("👋 Welcome to the math quiz 👋")
user_name = input("   What's your name? ")
print(f"Hello {user_name}!\n")

# Ask how many questions
while True:
    try:
        number_of_questions = int(input("How many questions would you like? (1 - 30): "))
        if 1 <= number_of_questions <= 30:
            break
        else:
            print("Please enter a number from 1 to 30.")
    except:
        print("Please enter a valid number.")

# Ask what type of question they want (once)
while True:
    type_of_question = input("Would you like: +, -, addition, subtraction, 1 or 2?\n").lower()
    if type_of_question in ["+", "addition", "1"]:
        question_type = "addition"
        break
    elif type_of_question in ["-", "subtraction", "2"]:
        question_type = "subtraction"
        break
    else:
        print("Please enter +, -, addition, subtraction, 1 or 2.")

# Define the quiz function
def run_quiz(num_questions, question_type):
    score = 0
    wrong_answers = []

    for i in range(1, num_questions + 1):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        if question_type == "addition":
            correct = num1 + num2
            symbol = "+"
        else:
            correct = num1 - num2
            symbol = "-"

        print(f"Question {i}: What is {num1} {symbol} {num2}?")
        try:
            user_answer = float(input("Your answer: "))
        except:
            print("That's not a number. Skipping question.\n")
            continue

        if user_answer == correct:
            print("✅ Correct!\n")
            score += 1
        else:

            print(f"❌ Wrong. The correct answer is {correct}\n")
            wrong_answers.append((f"Question {i}", correct, user_answer))

    return score, wrong_answers

# Run the quiz and get results
score, wrong_answers = run_quiz(number_of_questions, question_type)

# Show results
question = input("Would you like to see the game results? (yes/no) ").lower()
if question == "yes":
    print(f"\n*** Game Results ***\nScore: {score} / {number_of_questions}")
else:
    print(f"Ok. Thank you {user_name} for playing!")

# Show correct answers if wanted
see_wrong = input("Do you want the answers for the questions you got wrong? (yes/no) ").lower()
if see_wrong == "yes":
    for item in wrong_answers:
        print(f"{item[0]} ❌ Correct: {item[1]}, Your answer: {item[2]}")
else:
    print(f"Ok. Thank you {user_name} for playing!")