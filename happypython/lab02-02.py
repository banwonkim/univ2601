#lab02-02.py
userName=input('이름 ===> ')
userPhone=input('전화번호 ===> ')
print('제 이름은', userName, '이고, 연락처는', userPhone, '입니다.')

print("## 택배를 보내기 위한 정보를 입력하세요. ##")
personName = input("받는 사람 : ")
personAddr = input("주소 : ")
weight = int(input("무게(g) : "))

print("** 받는 사람 ==>", personName)
print("** 주소 =>", personAddr)
print("** 배송비 ==>", weight*5, "원")
