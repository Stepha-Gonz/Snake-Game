from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0,280)
        self.score=0
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.score_increment()

    def update_score(self):
            self.clear()
            self.write(arg=f"Score: {self.score} , High Score: {self.high_score}", align="center", font=('Arial', 15, 'normal'))
    

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt","w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_score()
    
    def score_increment(self):
        self.score+=1
        self.update_score()