from game import Game

game=Game()

print("Welcome to the Quiz Game!")
print("You will be presented with questions, and you need to provide the correct answers(True or False).")
is_going=True
while is_going:
    question = game.randomizer()
    print(f"question : {question}")
    answer=input("Your answer (true or false): ")
    is_going=game.condition(question,answer)
    print(is_going)

