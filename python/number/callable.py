# 'int' object is not callable

# Explanation : The “int object is not callable” error occurs when you declare a variable and name it with a built-in function name such as int() , sum() , max() , and others. The error also occurs when you don't specify an arithmetic operator while performing a mathematical operation.

# code that caused the error : 
vx = -b(2*a)
vy = a*(vx**2) + b*vx + c
print(f'Vertex: ({vx},{vy})')

# To solve the problem I had to add the asterix multiplier symbol as show here
vx = -b*(2*a)
vy = a*(vx**2) + b*vx + c
print(f'Vertex: ({vx},{vy})')
