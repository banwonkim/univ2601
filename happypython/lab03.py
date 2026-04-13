pound=int(input("파운드(lb) 입력:"))
kg=pound*0.453592
print(pound,"파운드(lb)는", kg, "킬로그램(kg)입니다.")

kg=int(input("킬로그램(kg)을 입력:"))
pound = kg*2.204623
print(kg,"킬로그램(kg)은", pound, "파운드(lb)입니다.")

# 1장 1 3 5 6 8
# 2장 5 7 8 9
# 3장 3 4 6 9 10

#lab03-02.py
total=0
total-=900*100
total-=3500*5
total+=1800*2
total+=4000*4
total+=1500
total+=2000*4
total+=1800*5
print("오늘 총 매출액 : ",total);

#lab03-03.py
python=3
mobile=2
excel=1

A=4.5
A0=4.0
B=3.5

avg = ((python * B) + (mobile * A0) + (excel * A)) / (python + mobile + excel)

print('평균 학점 :', avg)

#turtle
import turtle, random
turtle.shape("turtle")
turtle.pensize(1) # 펜의 두께: 5
turtle.pencolor("blue") # 펜의 색상: 파란색
while True :
    angle = int(input("거북이의 회전 각도 : "))
    distance = int(input("거북이의 이동 거리 : "))
    time=int(input('times:'))
    for i in range(time):
        turtle.right(angle)
        turtle.forward(distance)
