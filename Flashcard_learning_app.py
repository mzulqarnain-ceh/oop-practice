# Flashcard Learning App (OOP based)
import os
import json
folder=os.path.dirname(__file__)
path=os.path.join(folder,"flashcards.json")
# Class Flashcard
class Flashcard:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer
        self.attempts=0
        self.correct_count=0
    def check_answer(self,user_answer):
        self.attempts+=1
        if user_answer.lower()==self.answer.lower():
            self.correct_count+=1
            return True
        else:
            return False
class FlashcardDeck:
    def __init__(self,cards):
        self.cards=cards
        self.current=0
    def get_next_card(self):
        if self.current<len(self.cards):
            card=self.cards[self.current]
            self.current+=1
            return card
        else:
            return None
    def show_summary(self):
        total=len(self.cards)
        total_correct=0
        for card in self.cards:
            total_correct+= card.correct_count
        percentage=(total_correct/total)*100
        print(f"Total Cards: {total} | Total correct: {total_correct} | Percentage: ({percentage:.1f}%)")
        if percentage>=80:
            print("Excellent!")
        elif percentage>=50:
            print("Good Work")
        else:
            print("Keep Practicing")
def load_cards():
    try:
        with open(path,"r") as f:
            card=json.load(f)
            return [Flashcard(c["question"],c["answer"]) for c in card]
    except (FileNotFoundError,json.JSONDecodeError):
        print("File not found or may be corroupted")
        return []
def run_flashcards(cards):
    if len(cards)==0:
        print("No Card Avaiable")
        return
    card=FlashcardDeck(cards)
    while True:
        q_card=card.get_next_card()
        if q_card is None:
            break
        print(f"\n Q{card.current}: {q_card.question}")
        ans=input("Enter your answer: ")
        if q_card.check_answer(ans):
            print("Correct")
        else:
            print(f"Wrong! Correct answer: {q_card.answer}")
    card.show_summary()
# Entry point
if __name__=="__main__":
    cards=load_cards()
    run_flashcards(cards)