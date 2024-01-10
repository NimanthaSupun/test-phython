


count=int(input("Enter number of value: "))

total=0

for x in range(1,count+1):
   number=int(input(f"Enter number value {x}: "))
   
   total+=number
   
average=total/count

print(f"Total is : {total}")
print(f"Average is : {average}")

