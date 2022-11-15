from turtle import Turtle
SNAKE_X_START = [0, -20, -40]
MOVE_DISTANCE = 20

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
  
  def create_snake(self):
    for snake_segment in range(0, 3):
      new_snake_segment = Turtle()
      new_snake_segment.shape('square')
      new_snake_segment.color('white')
      new_snake_segment.penup()
      new_snake_segment.goto(SNAKE_X_START[snake_segment], 0)
      # new_snake_segment.forward(100)
      self.segments.append(new_snake_segment)


    def move(self):
      for seg_num in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)
      self.segments[0].forward(MOVE_DISTANCE)   