import random
import data
class Game:
    def randomizer(self):
        quiz=data.QNA
        return random.choice(list(quiz))
    def condition(self,question,answer):
        t_ans=data.QNA[question]
        if str(t_ans).lower()==answer.lower():
            print("Correct")
            data.score+=1
            data.num_question+=1
            print(f"Your score is {data.score}/{data.num_question}")
            return True
        else:
            print("Wrong")
            data.num_question+=1
            print(f"The correct answer is {t_ans}")
            print(f"your total score is {data.score}/{data.num_question}")
            return False




