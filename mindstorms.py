import turtle

def draw_polygon(some_turtle,sides,length):
    for i in range(0,sides):
        some_turtle.forward(length)
        some_turtle.left(360/sides)


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("green")

    dist=100
    sides=10

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.speed(5)


    for i in range(0,sides):
        draw_polygon(brad,4,dist)
        brad.left(360/sides)

    #angie=turtle.Turtle()
    #angie.shape("circle")
   # angie.color("blue")
   # angie.circle(dist)

   # alice=turtle.Turtle()
  #  alice.shape("turtle")
   # alice.color("red")

    #sides=0

    #while (sides<3):
     #   alice.forward(dist)
      #  alice.left(360/3)
      #  sides=sides+1
    #

    window.exitonclick()

draw_shapes()
