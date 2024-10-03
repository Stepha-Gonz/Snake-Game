import turtle as t
INITIAL_POSITIONS=[(0,0),(-20,0), (-40,0)]
MOVE_DISTANCE=20
UP=90
LEFT=180
DOWN=270
RIGHT=0
class Snake:

    def __init__(self):
        self.segments_list=[]
        self.snake_start()
        self.head=self.segments_list[0]
    def snake_start(self):

        for i in INITIAL_POSITIONS:
            self.add_segment(i)


    def add_segment(self,position):
        new_seg = t.Turtle("square")
        new_seg.speed("slowest")
        new_seg.penup()
        new_seg.color("white")
        new_seg.setpos(position)
        self.segments_list.append(new_seg)

    def extend(self):
        self.add_segment(self.segments_list[-1].position())

    def snake_animation(self):
        for seg in range(len(self.segments_list)-1,0,-1):
            new_x=self.segments_list[seg-1].xcor()
            new_y=self.segments_list[seg-1].ycor()
            self.segments_list[seg].goto(new_x,new_y)

        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)