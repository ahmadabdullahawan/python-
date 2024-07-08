def addition(x: object, y: object):
    sum = x + y
    return sum


results = addition(9, 10)
print("the sum is ", results)


def my_function(x):
    for i in x:
        print(i)


list = ["apple", "banana ", "cherry"]
my_function(list)

#function with default parameter

def function_peerson(name= "world ") :
    print ("hello " , name)

# calling the function with  default arguments
function_peerson()

# calling the function with arguments
function_peerson("abdullah")