import turtle
import os
import math
import random

#create screen
scr = turtle.Screen()
scr.setup(width=600 ,height=400)
scr.bgcolor("black")
scr.title("Space Game by Sanjeev Kumar")
scr.bgpic("background.gif")

sc = 0
# Score earned
score = turtle.Turtle()
score.penup()
score.speed(0)
score.color("red")
score.setposition(-280,160)
fun = "Score: %s" %sc
score.write(fun , False, align="left", font=("Arial",10))
score.hideturtle()

#Register shapes
turtle.register_shape("ship.gif")
turtle.register_shape("bot.gif")
turtle.register_shape("bullet.gif")

#Create bullet
bullet = turtle.Turtle()
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.setposition(0,-140)
bullet.hideturtle()

bulletspeed = 25

bulletstate = "ready"


#Draw the player
player = turtle.Turtle()
player.shape("ship.gif")
player.penup()
player.speed(0)
player.setposition(0,-160)

#Draw the bots 
no_bots = 7
bots = []
for i in range(no_bots): 
    bots.append(turtle.Turtle())
for bot in bots:    
    bot.shape("bot.gif")
    bot.penup()
    bot.speed(0)
    x = random.randint(-280, 280)
    y = random.randint(0, 140)
    bot.setposition(x,y) 
    botspeed = 2


# Move player left and right

playerspeed = 15 
def move_l():
    x = player.xcor()
    x -= playerspeed
    if x<-280:
        x = -280
    player.setx(x)

def move_r():
    x = player.xcor()
    x += playerspeed
    if x>280:
        x = 280
    player.setx(x)

def Fire():

    global bulletstate
    if bulletstate == "ready":
        bulletstate="fire"
    x = player.xcor()
    y = player.ycor() + 20
    bullet.setposition(x,y)
    bullet.showturtle()

def Collision(s1,s2):
    dist = math.sqrt(math.pow(s1.xcor()-s2.xcor() ,2)+math.pow(s1.ycor()-s2.ycor() ,2))
    if dist < 15:
        return True
    else:
        return False

#Create keyboard binding
turtle.listen()
turtle.onkey(move_l,"Left")
turtle.onkey(move_r,"Right")
turtle.onkey(Fire, "space")



#Move the bot
while True:
    for bot in bots:
        # Move the bot
        x = bot.xcor()
        y = bot.ycor()
        x += botspeed
        bot.setx(x)

        # Move bot back and down
        if bot.xcor() > 280:
            for b in bots:
                y = b.ycor()
                y -=20                
                b.sety(y)
            botspeed*=-1 
        if bot.xcor() < -280:
            for b in bots:
                y = b.ycor()
                y -=20
                b.sety(y)
            botspeed*=-1

        if bot.ycor() < -170:
            for b in bots:
                x = random.randint(-280, 280)
                y = random.randint(0, 140)
                #bot.setposition(x,y)
                player.hideturtle()
                bot.hideturtle()
                print("GAME OVER")
                break

       
        if Collision(bullet , bot):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-140)
            x = random.randint(-280, 280)
            y = random.randint(0, 140)
            bot.setposition(x,y)
            sc += 10
            fun = "Score: %s" %sc
            score.clear()
            score.write(fun , False, align="left", font=("Arial",10))


        if Collision (player ,bot):
            player.hideturtle()
            bot.hideturtle()
            print("GAME OVER")
            break
    
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 160:
        bullet.hideturtle()
        bulletstate == "ready"
    
turtle.done()