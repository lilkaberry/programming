import turtle

turtle.home()

#aussen
turtle.circle(150)
turtle.left(90)
turtle.penup()
turtle.forward(225)

#erstes Auge
turtle.left(90)
turtle.forward(75)
turtle.pendown()
turtle.circle(30)

turtle.penup()
turtle.back(150)
#zweites Auge
turtle.pendown()
turtle.circle(30)
turtle.penup()

#smile
turtle.left(90)
turtle.forward(100)
turtle.left(270)
turtle.forward(150)
turtle.left(90)
turtle.pendown()
turtle.circle(75, 180)

#alternativ input("random text, press something")
turtle.exitonclick()
