##### Indentation may need to be adjusted ####
# 1.import the turtle library
# 2. write speed and place it at 0 inside open & closed parentheses
# 3. write bgcolor and place "skyblue" inside open & closed parentheses
#######Grass######
# 4. write penup and have open & closed parentheses
# 5. write goto inside the open & closed parentheses write -400, -100
# 6. write pendown and have open & closed parentheses
# 7. write color and place "limegreen" have open & closed parentheses
# 8. write begin_fill and have open & closed parentheses
# 9. create a for loop where the range is (2):
# 10. write forward and inside the open & closed parentheses have 800
# 11.write right and inside the open & closed parentheses have 90
# 12. write forward and inside the open & closed parentheses have 400
# 13. write right and inside the open & closed parentheses have 90
# 14. write end_fill and have open & closed parentheses
# Left Mountain
penup()
goto(-400, -100)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
  forward(300)
  left(120)
end_fill()
# Right Mountain
penup()
# 15. write goto inside the open & closed parentheses write 100, -100
pendown()
begin_fill()
for i in range(3):
  forward(300)
  left(120)
end_fill()
# Middle Mountain
penup()
# 16. write goto inside the open & closed parentheses write -160, -100
pendown()
color("gray")
begin_fill()
for i in range(3):
  forward(400)
  left(120)
end_fill()
# Middle Mountain Ice Cap
penup()
# 17. write goto inside the open & closed parentheses write -35, 120
pendown()
color("white")
begin_fill()
left(35)
forward(60)
right(90)
forward(30)
left(100)
#18. write forward and inside the open & closed parentheses have 45
right(85)
#19. write forward and inside the open & closed parentheses have 65
left(160)
forward(150)
end_fill()
# Left Mountain Ice Cap
penup()
goto(-215, 100)
pendown()
color("snow")
begin_fill()
forward(70)
left(120)
forward(75)
left(150)
forward(45)
right(90)
forward(45)
left(120)
end_fill()
# Right Mountain Ice Cap
penup()
goto(203, 80)
pendown()
begin_fill()
forward(95)
# 20. write right and inside the open & closed parentheses have 120
forward(80)
right(150)
forward(50)
left(70)
end_fill()
left(50)
# Sun
penup()
goto(-500, 350)
pendown()
color("yellow")
begin_fill()
circle(125)
end_fill()
# Tree
def tree():
  # Tree trunk
  color("saddlebrown")
  begin_fill()
  for i in range(2):
    forward(40)
    left(90)
    forward(10)
    left(90)
  end_fill()
  # Turn the turtle around
  forward(10)
  left(90)
  forward(5)
  # Leaves on tree
  color("forestgreen")
  begin_fill()
  circle(25)
  end_fill()
  right(90)
# Plant the first tree
penup()
goto(-25,-200)
pendown()
tree()
# Plant the second tree
penup()
goto(200,-150)
pendown()
tree()
# Plant the third tree
penup()
goto(300,-250)
pendown()
tree()
# Plant the fourth tree
penup()
goto(-300,-250)
pendown()
tree()
# Plant the fifth tree
penup()
goto(-200,-100)
pendown()
tree()
hideturtle()
