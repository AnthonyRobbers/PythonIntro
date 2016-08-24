
# coding: utf-8

# In[1]:

import turtle


# In[2]:

def draw_polygon(some_turtle,psides,length):
    for i in range(0,psides):
        some_turtle.forward(length)
        some_turtle.left(360/psides)



# In[3]:

def draw_fractal(some_turtle,size,fsides,recursion):
    draw_polygon(some_turtle,fsides,size)
    if (recursion>0):        
        for i in range(0,fsides):
            #print("recursion is",+recursion)
            draw_fractal(some_turtle,size/2,fsides,recursion-1)
            some_turtle.forward(size)
            some_turtle.left(360/fsides)
        



# In[ ]:




# In[4]:

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("green")

    dist=200
    recursion=4
    sides=3
    circle_perimiter_est=1800
    
    recursion=input("Number of Additional Layers?")
    sides=input("Number of Sides?")
    
    dist=circle_perimiter_est/sides

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.speed(0)


    draw_fractal(brad,dist,sides,recursion)
    window.exitonclick()


# In[5]:

draw_shapes()


# In[ ]:



