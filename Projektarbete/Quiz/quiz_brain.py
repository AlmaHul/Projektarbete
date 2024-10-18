class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0 # Initierar räknaren för frågorna till 0
        self.score = 0 # Initierar spelarens poäng till 0
        self.question_list = q_list # Sparar listan av frågor

    def still_has_questions(self):
        """Kontrollerar om det fortafarnde finns frågor att ställa"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Hämtar och presenterar nästa fråga"""
        # Hämtar den sktuella frågan
        current_question = self.question_list[self.question_number]
        # Ökar frågeräkningen för att gå till nästa fråga
        self.question_number += 1
        # Frågar användaren om svaret
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Kontrollerar om svaret är rätt
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Kontrollerar om användarens svar är korrekt"""
        # Jämför användarens svar med korrekta svaret
        if user_answer.lower() == correct_answer.lower():
            self.score += 1 # Ökar poängen om svaret är korrekt
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")