import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        random.shuffle(self.questions)

        for question in self.questions:
            print(question["text"])
            self.display_options(question["options"])

            user_answer = input("Your answer: ").upper()

            if user_answer == question["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}\n")

        self.display_final_score()

    def display_options(self, options):
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def display_final_score(self):
        print(f"Your final score: {self.score}/{len(self.questions)}")

# Example questions
questions = [
    {
        "text": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "B"
    },
    {
        "text": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "B"
    },
    # Add more questions as needed
]

if __name__ == "__main__":
    quiz = QuizGame(questions)
    quiz.start_quiz()
