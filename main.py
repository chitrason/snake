"""Snake"""
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake_x_start = [0, -20, -40]
segments = []

for snake_segment in range(0, 3):
  new_snake_segment = Turtle()
  new_snake_segment.shape('square')
  new_snake_segment.color('white')
  new_snake_segment.penup()
  new_snake_segment.goto(snake_x_start[snake_segment], 0)
  # new_snake_segment.forward(100)
  segments.append(new_snake_segment)


game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  for seg_num in range(len(segments) - 1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(new_x, new_y)
  segments[0].forward(20)    









screen.exitonclick()
