a=int(input("enter number which you want to series"))
x=1;
y=1;
print(x);
print(y);
for i in range(1,a):
    count=x+y;
    print(count);
    x,y=y,count;