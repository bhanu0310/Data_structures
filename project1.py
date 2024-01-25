a=int(input("How Many Days Temperature?"))
list=[]
for i in range(a):
    print("Enter the day",i+1,"s temperature")
    k=int(input())
    list.append(k)
print("The Three days temperature is",list)
avg=((sum(list))/(len(list)))
print("The Average Temperature is",avg)
sum=0
for i in range(a):
    if list[i]>avg:
        sum+=1
if sum<1:
    print("There is no day tempearure greater than the average")
else:
    print("There are",sum,"no of days that are greater than the avg temperature")
