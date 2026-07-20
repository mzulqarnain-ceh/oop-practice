import os
import json
folder=os.path.dirname(__file__)
path=os.path.join(folder,"questions.json")
# Question class
class Question:
    def __init__(self,question,options,answer):
        self.question=question
        self.options=options
        self.answer=answer
    def check_answer(self,user_answer):
        return user_answer==self.answer
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.current=0
    def get_next_question(self):
        if self.current<len(self.questions):
            question=self.questions[self.current]
            self.current+=1
            return question
        else:
            return None
    def show_score(self):
        total=len(self.questions)
        percentage=(self.score/total)*100
        print(f"\nFinal Score: {self.score}/{total} Percentage ({percentage:.1f}%)")
        if percentage>=80:
            print("Excellent!😊")
        elif percentage>=50:
            print("Good Work!")
        else:
            print("Keep Practicing!")
def load_questions():
    try:
        with open(path,"r") as f:
            questions=json.load(f)
        return [Question(q["question"],q["options"],q["answer"]) for q in questions]
    except (FileNotFoundError,json.JSONDecodeError):
        print("File not found or may be corrupted")
        return []
def run_quiz(questions):
    if len(questions)==0:
        print("No questions are available")
        return
    quiz=Quiz(questions)
    while True:
        question=quiz.get_next_question()
        if question is None:
            break
        print(f"\nQ{quiz.current}: {question.question}")
        for i,option in enumerate(question.options):
            print(f" {i+1} {option}")
        try:
            choice=int(input("Enter your answer (1-4): "))
            if choice<1 or choice>len(question.options):
                print("Please enter a number between (1-4). Skipping this question")
                continue
        except ValueError:
            print("Please enter a valid number between (1-4). Skipping this question")
            continue
        user_answer=question.options[choice-1]
        if question.check_answer(user_answer):
            print("Correct")
            quiz.score+=1
        else:
            print(f"Wrong! Correct answer: {question.answer}")
    quiz.show_score()
# starting point
if __name__ == "__main__":
    questions=load_questions()
    run_quiz(questions)