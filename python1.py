print('hello world')
# hello am abdullah am writing a single line comment
'''
multiline comment
'''
# variable declaration
a = 10
print(type(a))
print(a)

b = 'abdullah'
type(b)

c=10
print(c+10)
print(c*10)
print(c/2)
print(c%2)

#bool
l1 = True
l2 = type(l1)
print(l2)

m1 = 'abdullah'
print(m1)
v0 = m1+'ahmad'
print(v0)
v1 = m1 + str(1)
print(v1)

#complex numbers
a9= 9.0 + 10j
print(a9)
print(a9.real,a9.imag)

# Dynamic typing
x = 10  # x is an integer
x = "hello"  # x is now a string

# Strong typing (implicit conversion not allowed)
x = 10
y = "20"
'''
result = x + y  # This will raise a TypeError because you can't add an integer and a string
'''

#getting inputs
a7=input('enter number')
a8=input('enter a 2nd number')
print(a7+a8)

first_name='abdullah'
last_name='ahmad'
print('the first name is {z1} and last name is {z2}'.format(z1=first_name,z2=last_name))
