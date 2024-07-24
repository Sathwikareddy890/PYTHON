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
# 9PRONLEM find the elements that is present in k+n index k is given by  user (n=2)
'''my_list=list(map(int,input().split(" ")))
k=int(input("enter k value"))
n=2
length=len(my_list)
if length<k+n:
    print("error")
else:
    for i in range(0,len(my_list)):
            print(my_list[k+n],end=" ")
            break'''

''''#PROBLEM 10 you are suppose to print the element in a particular index by cyclic printing
my_list=list(map(int,input().split(" ")))
k=int(input("k"))
i=1
for i in range(1,len(my_list)):
    num=my_list[k%len(my_list)]
print(num)'''

#find the max element in a given list

'''my_list=list(map(int,input().split(" ")))
i=0
max=my_list[i]
for i in range(len(my_list)):
    if (my_list[i]>max):
        max=my_list[i]
print(max)'''


#find the minimum element in a given list

'''my_list=list(map(int,input().split(" ")))
i=0
max=my_list[i]
for i in range(len(my_list)):
    if (my_list[i]<max):
        max=my_list[i]
print(max)'''


# PROBLEM 12 replace the elements in an array with a avg of max and min element

#find the max element in a given list

'''my_list=list(map(int,input().split(" ")))
i=0
min=my_list[i]
for i in range(len(my_list)):
    if (my_list[i]<min):
        min=my_list[i]
print(min)
max=my_list[i]
for i in range(len(my_list)):
    if (my_list[i]>max):
        max=my_list[i]
print(max)
avg=(min+max)//2
print(avg)
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)'''
#find the missing number in an array
'''my_list=list(map(int,input().split(" ")))
i=0
sum=0
n=int(input('enter n'))
t=(n*(n+1))/2
for i in range(i,len(my_list)):
     sum+=my_list[i]
miss=t-sum
print(miss)'''

#remove duplicate duplicate element in an array
'''my_list=list(map(int,input().split(" ")))
i=0
new_list=[]
for i in range(i,len(my_list)):
     if my_list[i] in new_list:
          print("")
     else:
          new_list.append(my_list[i])
          print(new_list)'''

'''my_list=list(map(int,input().split(" ")))
new_list=[]
for i in my_list:
     if i not in new_list:
          new_list.append(i)
print(new_list)'''















