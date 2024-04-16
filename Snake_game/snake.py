from turtle import Turtle,Screen

STARTING_POS = [(0,0), (-20,0), (-40,0)] #tuples coordonate
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

        #default size = 20..
        def __init__(self):
                self.body_list = []
                self.create_snake()
                self.head = self.body_list[0]
        
        def create_snake(self):
              for position in STARTING_POS:
                self.add_body(position)


        def add_body(self, position):
            new_body = Turtle(shape="square")
            new_body.color("white")
            new_body.penup()
            new_body.goto(position)
            self.body_list.append(new_body)

        def extend(self):
             self.add_body(self.body_list[-1].position())  #self.bodylist[-1] = ultimul body
             

        def move(self):
            for body_num in range(len(self.body_list) - 1, 0, -1):    # range(start = len(body_list) - 1, stop = 0, step = -1)    #step = cum ajungi de la start la stop
                new_x = self.body_list[body_num-1].xcor()
                new_y = self.body_list[body_num-1].ycor()
                self.body_list[body_num].goto(new_x, new_y)
            self.body_list[0].forward(MOVE_DISTANCE)

        def reset_snake(self):
             for bodys in self.body_list:
                  bodys.goto(1000,1000)#mutam random undeva bodyurile vechi
             self.body_list.clear()#remove toate body-urile
             self.create_snake()
             self.head = self.body_list[0]

        def up(self):
            if self.head.heading() != DOWN:
                self.head.seth(UP)
        def down(self):
            if self.head.heading() != UP:
                self.head.seth(DOWN)
        def left(self):
            if self.head.heading() != RIGHT:
                self.head.seth(LEFT)
        def right(self):
            if self.head.heading() != LEFT:
                self.head.seth(RIGHT)