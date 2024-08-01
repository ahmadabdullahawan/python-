for i in range(10):
    print("hello world")
print('THE ABOVE GONNA PRINT HELO WORLD')

list = ["apple", "banana", "cherry"]
for x in list:
    print(x)
print("the above gonna print the above list ")

set = {1, 2, 3, 4, 5, 6}
for i in set:
    print(i)
print("the above gonna print the above set")

a = "banana"
for x in a:
    print(x)
print("the above gonna print the above string individually ")

#forloop
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i ** 2)

print("for loop ended")

#finding the sum of all elements in a list
list2 = [1, 2, 3, 4, 5, 6]
sum = 0
for i in list2:
    sum= sum + i
print(sum)
print("for loop ended")

#making a list using for loop

lit = []
for i in range(10):
    h = float(input("enter a number: "))
    lit.append(h)
print(lit)
even_sum=0
odd_sum=0
for i in lit:
    if (i%2==0):
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
print(even_sum)
print(odd_sum)
## while condition

i = 0
even_sum = 0
odd_sum = 0
while (i <= 10):

    if (i % 2 == 0):
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

    i = i + 1
print(even_sum, odd_sum)
##break
x = 1
while (x < 7):

    if x == 4:
        break
    print(x)
    x = x + 1
    ## continue
    x = 0
    while x < 7:
        x = x + 1
        if x == 4:
            continue
        print(x)



