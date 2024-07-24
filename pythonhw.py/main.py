# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#printing even and odd numbers
'''num=int(input("enter the number"))
if num%2==0:
    print("the given num is even")
else:
    print(f"given number i.e {num} is odd number")'''

#greatest of three numbers
'''a=int(input("enter first value"))
b=int(input("enter second value"))
c=int(input("enter thrid value"))
if a>b and a>c:
    print("first value is the greatest value")
elif b>a and b>c:
    print("second value  is the greatest value")
else:
    print("thrid value  is the greatest value")'''

#sum of the elements
'''my_list=list(map(int,input("enter values to the list").split()))
i=0
sum=0
for i in range(i,len(my_list)):
    sum=sum+my_list[i]
print(sum)'''

#printing the peak elements
'''my_list=list(map(int,input("enter the values to the array").split(" ")))
n=len(my_list)
peak=[]
for i in range(n):
    if(i==0 and my_list[i]>=my_list[i+1]):
        peaks.append(my_list[i])
print("peak elements:",peaks)'''

#reverse of a number
'''n=int(input("enter n"))
rev=" "
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))'''

#sum of even and odd digits
'''n=list(map(int,input("enter the values").split(",")))
sum=0
sum2=0
i=0
for i in range(i,len(n)):

    if n[i] % 2==0:
        sum=sum+n[i]
    print("sum of even numbers is",sum)
else:
    sum2=sum2+n[i]
    print("sum of odd numbers is",sum2)'''






