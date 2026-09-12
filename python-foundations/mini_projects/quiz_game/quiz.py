"""
quiz.py

Mini Project: Quiz Game
Covers: lists of tuples | loops | scoring logic | conditional feedback
"""

quiz_questions = [
    ("What is the capital of France?", ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "C"),
    ("Which language is this file written in?", ["A. Java", "B. Python", "C. C++", "D. HTML"], "B"),
    ("What does CPU stand for?", ["A. Central Process Unit", "B. Computer Personal Unit",
                                    "C. Central Processing Unit", "D. Central Processor Utility"], "C"),
    ("2 + 3 * 2 equals?", ["A. 10", "B. 8", "C. 12", "D. 7"], "B"),
]


def run_quiz():
    score = 0
    total_questions = len(quiz_questions)

    for question_number, (question_text, options, correct_answer) in enumerate(quiz_questions, start=1):
        print(f"\nQ{question_number}. {question_text}")
        for option in options:
            print(f"  {option}")

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer: {correct_answer}")

    return score, total_questions


def display_result(score, total_questions):
    percentage = (score / total_questions) * 100

    print("\n----- QUIZ RESULT -----")
    print(f"Score: {score}/{total_questions} ({percentage:.1f}%)")

    if percentage >= 75:
        remark = "Excellent work!"
    elif percentage >= 50:
        remark = "Good effort, keep practicing."
    else:
        remark = "Needs improvement, try again."

    print(remark)


def main():
    print("----- QUIZ GAME -----")
    print(f"Answer all {len(quiz_questions)} questions. Good luck!\n")

    score, total_questions = run_quiz()
    display_result(score, total_questions)


if __name__ == "__main__":
    main()
