#한줄 이어붙이기
for i in range(3):
  print('👻', end='')
#한줄씩 새줄로 출력하기
for i in range(3):
  print('👻')
#한줄씩 띄어 출력하기
for i in range(3):
  print('👻\n')
  
#0~9 출력
for i in range(10):
  print(i,end="_")
for i in range(0,10):
  print(i,end="_")
print("...end")

#리스트의 요소 출력
hi=["I","AM","YOUR","FATHER"]
for i in hi:
  print(i)

#while 조건식:
#조건식이 True 일 떄 실행
count=0
while True:
  print("what??")
  count+=1
  if count==3:
    break