import turtle

def draw_polygon(some_turtle,psides,length):
    for i in range(0,psides):
        some_turtle.forward(length)
        some_turtle.left(360/psides)



def draw_fractal(some_turtle,size,fsides,recursion):
    draw_polygon(some_turtle,fsides,size)
    if (recursion>0):        
        for i in range(0,fsides):
            #print("recursion is",+recursion)
            draw_fractal(some_turtle,size/2,fsides,recursion-1)
            some_turtle.forward(size)
            some_turtle.left(360/fsides)
        


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("green")

    dist=200
    recursion=2
    sides=36
    circle_perimiter_est=2000
    
    dist=circle_perimiter_est/sides

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.speed(0)


    draw_fractal(brad,dist,sides,recursion)
    window.exitonclick()

draw_shapes()
