var1 = input("첫 번째 문자열 ==>")
var2 = input("두 번째 문자열 ==>")
len1 = len(var1)
len2 = len(var2)
diff = abs(len1 - len2)
print("두 문자열의 길이 차이는", diff, "입니다.")


print("\n줄바꿈\n연습 ")
print("\t탭키\t연습")
print("어떤 글자를 \"강조\"하는 효과1")
print("어떤 글자를 \'강조\'하는 효과2")
print("\\\\ 백슬래시 2개 출력")

var3="난생두번째 python"
print(len(var3))

ss='second python'
print(ss.isupper())
print(ss.islower())
print('count of o in "', ss, '" is ', ss.count('o'),sep='')

ss='my memory'
print(ss)
print(ss.find('m'))
print('rev==>', ss[::-1])

ss2=''
ss2+=ss[0].upper()
ss2+=ss[1].upper()
ss2+=ss[2].upper()

print(ss2)


ss = "Python"
print("원본문자열==>", ss)
ss2 = ""
ss2 += ss[0].lower( )
ss2 += ss[1].upper( )
ss2 += ss[2].upper( )
ss2 += ss[3].upper( )
ss2 += ss[4].upper( )
ss2 += ss[5].upper( )
print(ss2)


#turtle
import turtle
turtle.shape('turtle')
turtle.penup()

while True:
    tcol=input('pen color(red,blue,green,yellow,magenta):')
    x=int(input('loc x:'))
    y=int(input('loc y:'))
    text=input('letter:').upper()

    turtle.pencolor(tcol)
    turtle.goto(x,y)
    turtle.write(text, font=('Arial', 30))

turtle.done()
