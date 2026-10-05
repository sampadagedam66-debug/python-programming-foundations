import random

# -----------------------------
# Python Quiz Game
# -----------------------------

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for a comment in Python?",
        "options": ["A. //", "B. <!-- -->", "C. /* */", "D. #"],
        "answer": "D"
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A. add()", "B. append()", "C. insert()", "D. push()"],
        "answer": "B"
    },
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which collection does NOT allow duplicate values?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. String"],
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. get()", "B. scan()", "C. input()", "D. read()"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["A. /", "B. //", "C. %", "D. **"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a loop over a sequence?",
        "options": ["A. repeat", "B. loop", "C. for", "D. iterate"],
        "answer": "C"
    },
    {
        "question": "Which file extension is used for Python files?",
        "options": ["A. .java", "B. .py", "C. .python", "D. .pt"],
        "answer": "B"
    }
]


def display_question(number, question):
    print(f"\nQuestion {number}")
    print("-" * 40)
    print(question["question"])

    for option in question["options"]:
        print(option)


def run_quiz():
    score = 0

    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    print("\n" + "=" * 45)
    print("        🐍 PYTHON QUIZ CHALLENGE")
    print("=" * 45)
    print("Test your Python fundamentals!")

    for number, question in enumerate(quiz_questions, start=1):
        display_question(number, question)

        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("⚠️ Please enter A, B, C, or D.")

        if user_answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {question['answer']}")

    percentage = (score / len(quiz_questions)) * 100

    print("\n" + "=" * 45)
    print("              QUIZ RESULT")
    print("=" * 45)

    print(f"Score      : {score}/{len(quiz_questions)}")
    print(f"Percentage : {percentage:.1f}%")

    if percentage == 100:
        print("🏆 Perfect Score! Python master!")
    elif percentage >= 80:
        print("🌟 Excellent! Your fundamentals are strong.")
    elif percentage >= 60:
        print("👍 Good job! Keep practicing.")
    elif percentage >= 40:
        print("📚 Not bad! Revise your Python basics.")
    else:
        print("💪 Keep learning. You will improve!")

    print("=" * 45)


while True:
    run_quiz()

    play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()

    if play_again != "Y":
        print("\nThanks for playing! 👋")
        break