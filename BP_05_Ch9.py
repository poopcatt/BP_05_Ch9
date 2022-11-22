#기초파이썬 9장 연습문제 터틀그래픽



#4. 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 사각형을 그리는 프로그램을 작성해보자.

import random                                #랜덤 값 불러오기
import turtle
t=turtle.Turtle()
t.shape("turtle")
color=["yellow","red","purple","blue"]       #색상 리스트 지정

def draw_square(x,y,z):                      #draw_square(x,y,z) 함수 생성
    t.up
    t.goto(x,y)
    t.down
    t.color(z)
    t.begin_fill()
    for i in range(4):                       #4번 반복
        t.forward(50)
        t.left(90)
    t.end_fill()

for z in color:                              #리스트의 색 반복
    x=random.randint(-200,200)
    y=random.randint(-200,200)               #x좌표와 y좌표를 (-200,200) 내에서 무작위로 정함
    draw_square(x,y,z)
t.screen.exitonclick()


#5. 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 다각형을 그리는 프로그램을 작성해보자.

import random
import turtle
t=turtle.Turtle()
t.shape("turtle")
color=["red","blue","brown","yellow","green","purple"]      #색상 리스트 지정
length=0
sides=0
x=0
y=0                                                         #길이,변, x좌표,y좌표를 0으로 고정 후 시작

def draw_shape(t,z,length,sides,x,y):                       #draw_shape(t,z,length,sides,x,y) 함수 생성 (다각형이라 여러 종류가 생길수 있음)
    t.up()
    t.goto(x,y)
    t.down()
    t.color(z)
    t.begin_fill()
    for i in range(sides):                                  #변의 수만큼 반복
        t.forward(length)                                   #후술할 랜덤값의 길이만큼 전진
        t.left(360/sides)                                   #n각형이면 360/n만큼 좌측으로 기울임
    t.end_fill()

for z in color:
    sides=random.randint(3,8)                               #변의 수는 3 이상 8 이하로 랜덤하게 생성
    x=random.randint(-250,250)
    y=random.randint(-250,250)                              #x좌표와 y좌표를 (-250,250) 내에서 무작위로 설정
    length=random.randint(10,50)                            #길이를 10 이상 50 이하로 랜덤하게 설정
    draw_shape(t,z,length,sides,x,y)
t.screen.exitonclick()


#6. 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 별을 그리는 프로그램을 작성해보자.

import random
import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.Screen()
s.bgcolor("black")
color=["red","blue","brown","yellow","green","purple","white"]   #색상 리스트 지정
length=0
sides=0
x=0
y=0                                                              #길이, 변, x좌표, y좌표를 0으로 고정 후 시작

def Ode_to_the_stars(color,length,x,y):                          #Ode_to_the_stars(color,length,x,y) 함수 생성
    t.up()
    t.goto(x,y)
    t.down()
    t.color(z)
    for i in range(5):                                           #별은 5개의 변 (5번 반복)
        t.forward(length)                                        #후술할 랜덤값의 길이만큼 전진
        t.left(144)
    t.end_fill()
    
for z in color:
    x=random.randint(-300,300)
    y=random.randint(-300,300)                                   #x좌표와 y좌표를 (-300,300) 내에서 무작위로 설정
    length=random.randint(10,50)                                         #길이는 10 이상 50 이하로 랜덤하게 설정
    Ode_to_the_stars(color,length,x,y)                           #노래좋다
t.screen.exitonclick()
