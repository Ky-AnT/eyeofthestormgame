from turtle import *
import random
import time
from turtle import Turtle, Screen, Shape
import math
from threading import Thread
import pygame
from playsound import playsound
def play_music():
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the music file
    pygame.mixer.music.load("background.wav")
    # Play the music on loop
    pygame.mixer.music.play(-1)
    pygame.mixer.music.queue("background.wav")

music_thread = Thread(target=play_music)
music_thread.start()
window = Screen()
listening = True
#window.setup(width=600, height=600)
window.screensize(canvwidth=700, canvheight=700)
window.setup(750,750)
window.title("Eye of the Storm")
window.bgpic('background_image.png')
head = Turtle()
window.tracer(0)
score = 0
window.register_shape("brick_layers/1.gif")
head.shape("brick_layers/1.gif")
#width, height,none = head.shapesize()
#scaling_factor = 0.5
#head.shapesize(width * scaling_factor, height * scaling_factor)
#head.shapesize(20)

#Variable to check if bullet is available to shoot
done = True

def get_coor(x,y):
    global done
    if done != False and creditNum == 0 and listening == True:
        createBullet(x,y)

#createBullet function, to create a bullet to shoot enemies. The bullet disappears after
#reaching mouse pointer co-ordinates

def createBullet(x,y):
    global done, score
    done = False
    bullet = Turtle()
    window.register_shape("bullet_gif.gif")
    bullet.shape("bullet_gif.gif")
    bullet.penup()
    #bullet.shapesize(1/3,1/3)
    #While the bullet has not reached the mouse pointer yet
    while (max(bullet.xcor(),x)-min(bullet.xcor(),x) < 20 and max(bullet.ycor(),y)-min(bullet.ycor(),y) < 20) != True:
        #print(done)
        #Tilt the bullet towards the mouse pointer
        bullet.setheading(bullet.towards(x, y))
        bullet.tiltangle(bullet.heading())
        #print(enemy)
        #print(len(enemy))
        #For every object in the enemy list
        for n in range(len(enemy)):
            #print(n)
            #print(enemy[n])
            #if max(enemy[n].xcor(),bullet.xcor())-min(enemy[n].xcor(),bullet.xcor()) < 5 and max(enemy[n].ycor(),bullet.ycor())-min(enemy[n].ycor(),bullet.ycor()) < 5:
            if bullet.distance(enemy[n]) < 15:
                #print(True)
                enemy[n].goto(-700,700)
                enemy.remove(enemy[n])
                score += 1
                #print(enemy)
                #print(f"Length: {len(enemy)}")
                break
        bullet.forward(10)
        update()
    bullet.goto(-700,700)
    update()
    #print(done)
    done = True




#head.shapesize(1/3,1/3)
head.penup()
head.goto(0,-10)
#head.pendown()
update()

creditNum = 0
dimension = 350
enemy = []
def addEnemy():
    global dimension
    head.penup()
    obj = Turtle()
    #obj.shape("square")
    #obj.color("red")
    window.register_shape("enemies/enemy_1.gif")
    obj.shape("enemies/enemy_1.gif")
    #obj.shapesize(1/3,1/3)
    #side is a variable, which chooses which side of the screen to create enemies
    #Takes a square of 280*280, and places enemies on the borderline of the square
    side = random.randint(1,4)
    tempRand = random.randint(-7,7)*20
    if side == 1:
        obj.penup()
        #Moves the turtle object to the bottom side
        obj.setpos(tempRand,-dimension)
    elif side == 2:
        obj.penup()
        obj.setpos(tempRand,dimension)
    elif side == 3:
        obj.penup()
        obj.setpos(dimension+10,tempRand+10)
    elif side == 4:
        obj.penup()
        obj.setpos(-dimension-10,tempRand+10)
        #obj.setpos(-350,tempRand)
    enemy.append(obj)

#Functions to move the wall block in a certain direction
def right():
    head.penup()
    global creditNum, stamps
    if creditNum != 0:
        x = head.xcor()
        #print(f"Right: {head.pos()}")
        if (x+20,head.ycor()) != (0,10):
            stamps.append(head.stamp())
            segments.append(head.pos())
            head.setx(x+20)
            #print(segments)
            creditNum -= 1
            window.title(f"Eye of the Storm - Credits Left: {creditNum}")
def left():
    head.penup()
    global creditNum, stamps
    if creditNum != 0:
        x = head.xcor()
        #print(f"Left: {head.pos()}")
        #print(x-20)
        if (x-20,head.ycor()) != (0,10):
            stamps.append(head.stamp())
            segments.append(head.pos())
            head.setx(x-20)
            #print(segments)
            creditNum -= 1
            window.title(f"Eye of the Storm - Credits Left: {creditNum}")
def up():
    head.penup()
    global creditNum, stamps
    if creditNum != 0:
        y = head.ycor()
        #print(f"Up: {head.pos()}")
        #print(y+20)
        if (head.xcor(),y+20) != (0,10):
            stamps.append(head.stamp())
            segments.append(head.pos())
            head.sety(y+20)
            #print(segments)
            creditNum -= 1
            window.title(f"Eye of the Storm - Credits Left: {creditNum}")
def down():
    head.penup()
    global creditNum
    if creditNum != 0:
        #print(f"Down: {head.pos()}")
        y = head.ycor()
        #print(y-20)
        #print(head.xcor(),y-20)
        if (head.xcor(),y-20) != (0,10):
            stamps.append(head.stamp())
            segments.append(head.pos())
            head.sety(y-20)
            #print(segments)
            creditNum -= 1
            window.title(f"Eye of the Storm - Credits Left: {creditNum}")
window.listen()
window.onkey(right,"Right")
window.onkey(left,"Left")
window.onkey(up,"Up")
window.onkey(down,"Down")
segments = []
created = False
waveNum = 0
interval = 1
stamps = []
playerList = []
shrinkRate = 10
spawnNumber = 5

growthRate = 0.2
end = False
def moveEnemy():
    global stamps, segments, end, enemySpeed
    #print(segments)
    for i in range(len(enemy)):
        enemy[i].setheading(enemy[i].towards(0, 10))
        #bullet.tiltangle(bullet.heading())
        #print(waveNum)
        enemy[i].forward(enemySpeed)
        minResult = None
        savedN = None
        end_squared = ((max(enemy[i].xcor(),0)-min(enemy[i].xcor(),0))**2)
        end_two_squared = ((max(enemy[i].ycor(),10)-min(enemy[i].ycor(),10))**2)
        end_result = round(math.sqrt(end_squared+end_two_squared),2)
        
        if end_result < 20:
            end = True
        for n in segments:
            #print(f"Stamps List: {stamps}")
            #print(f"Segments List: {segments}")
            a_squared = ((max(enemy[i].xcor(),n[0])-min(enemy[i].xcor(),n[1]))**2)
            b_squared = ((max(enemy[i].ycor(),n[1])-min(enemy[i].ycor(),n[1]))**2)
            result = round(math.sqrt(a_squared+b_squared),2)
            #print(result)
            if minResult == None:
                minResult = result
                savedN = n
            elif result < minResult:
                minResult = result
                savedN = n
        if result < 35:
            print("Wall hit!")
            head.clearstamp(stamps[segments.index(savedN)])
            stamps.remove(stamps[segments.index(savedN)])
            segments.remove(savedN)
            enemy[i].backward(200)
            #addEnemy()
        else:
            #print("Not colliding")
            pass

def createPlayer():
    playerList.append(Turtle())
    #playerList[0].shape("square")
    #playerList[0].shapesize(1/3,1/3)
    playerList[0].penup()
    playerList[0].goto(0,10)
    window.register_shape("main_char.gif")
    playerList[0].shape("main_char.gif")
def wave(level):
    global spawnNumber
    for i in range(int(spawnNumber)):
        addEnemy()
    #print(spawnNumber)
addCredit = 0
enemySpeed = 0.1
def clearSegments():
    global creditNum, created, playerList, waveNum, segments, dimension, stamps, addCredit, enemySpeed
    window.title(f"Eye of the Storm")
    enemySpeed += 0.1
    for i in range(len(stamps)):
        head.clearstamp(stamps[i])
    stamps = []
    segments = []
    creditNum = 7+addCredit
    #print(creditNum)
    #print("set to false")
    created = False
    if len(playerList) != 0:
        playerList[0].hideturtle()
    waveNum += 1
    head.goto(0,-10)
    addCredit += 1
onscreenclick(get_coor)
#def loopSound():
#    while True:
#        playsound('background.wav', False)
#loopThread = Thread(target=loopSound, name='backgroundMusicThread')
#loopThread.daemon = True # shut down music thread when the rest of the program exits
#loopThread.start()

while True:
    # Wait for the sound to finish playing before playing it again
    while pygame.mixer.get_busy():
        pass
    if len(enemy) == 0:
        clearSegments()
        spawnNumber += round(spawnNumber*growthRate,0)
        wave(waveNum)
        dimension -= shrinkRate
        shrinkRate *= 0.9
        update()
    if creditNum == 0 and created == False:
        if len(playerList) == 0:
            createPlayer()
        else:
            playerList[0].showturtle()
        created = True
        update()
    if created == True:
        if done == True:
            window.title(f"Eye of the Storm - Wave {waveNum}")
            moveEnemy()
        else:
            pass
        update()
    if end == True:
        print("Game Over!!!")
        print(f"Your Score: {score}")
        listening = False
        break
    update()
window.mainloop()