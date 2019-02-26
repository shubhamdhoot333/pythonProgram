num=int(input("enter number 100 to 999 which you want to know armstrong number or not"))
temp=num
rem=newnum=0
while num:
    rem=num % 10
    newnum+=rem ** 3
    num=int(num//10)

if temp == newnum:
     print('yes')
else:
    print('no')