from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0,280)
        self.score=0
        self.score_increment()


    def score_increment(self):

        self.clear()
        self.write(move=False, arg=f"Score: {self.score}", align="center", font=('Arial', 15, 'normal'))
        self.score+=1

    def game_over(self):
        self.goto(0,0)
        self.write(move=False, arg="GAME OVER", align="center", font=('Arial', 15, 'normal'))