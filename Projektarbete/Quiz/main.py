from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


# Shuffle question_data för att få slumpmässiga frågor
random.shuffle(question_data)

# Skapar en lista med objekt av klassen Question.
question_bank = []  # Tom lista
for question in question_data: # Itererar genom en datakälla
    question_text = question["text"] # Hämtar texten av frågan
    question_answer = question["answer"] # Hämtar svaret av frågan
    new_question = Question(question_text, question_answer) # Skapa ett nytt frågeobjekt
    question_bank.append(new_question) # Lägger till det i listan


quiz = QuizBrain(question_bank)
print("Welcome to the True or False Quiz!")


# Loopen fortsätter så länge det finns frågor att ställa
while quiz.still_has_questions():
    # Fråga om användaren vill spela eller avbryta
    user_input = input("Write 'quit' to stop playing or press Enter to continue: ")
    if user_input.lower() == 'quit':
        print(f"You chose to end the game. Your total points are: {quiz.score}/{quiz.question_number}")
        break  # Avbryter loopen
    quiz.next_question()

print("You've completed the quiz")
# Skriver ut dina poäng
print(f"Your final score was: {quiz.score}/{quiz.question_number}")