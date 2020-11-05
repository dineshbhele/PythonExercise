# Exercise 1. Program showing value and type of the expression
"""  Assume that we execute the following assignment statements:
width = 17
height = 12.0
delimiter = '.'
For each of the following expressions, write the value and the type of the expression.
1. width/2
2. width/2.0
3. height/3
4. 1 + 2 * 5
5. delimiter * 5 """

width = 17
height = 12.0
delimiter = '.'

# The value is:8.5 and Type is: float
print(f"value of width/2 is:{width/2}")
print(f"Type of width/2 is:{type(width/2)}")

# The value is:8.5 and Type is : float
print(f"Value of width/2.0 is: {width/2.0}")
print(f"Type of Width/2.0 is: {type(width/2.0)}")

# The value is :4.0 and Type is :float
print(f"Value of height/3 is: {height/3}")
print(f"Type of height/3 is: {type(height/3)}")

# The Value is: 11 and Type is: int
print(f"Value of 1+2*5 is: {1+2*5}")
print(f"Type of 1+2*5 is: {type(1+2*5)}")

# The vlaue is: ..... and Type is: str
print(f"Value of .*5 is: {'.'*5}")
print(f"Type of .*5 is : {type('.'*5)}")

""" ........................................................................"""

# Exercise 2.Convert farenheit to celsius in degree
farenheit = float(input("Enter the Farenheit:"))
celsius = ((farenheit-32)*5)/9
print(f"{farenheit} Farenheit is {celsius} celsius")

""" ........................................................................"""

# Exercise 3. Write a program that takes seconds as time units and converts it to minutes and seconds
seconds = int(input("Enter the time as Seconds:"))
remainder_seconds = seconds % 60
minutes = int(seconds/60)
print(f"{seconds} seconds in {minutes} minute and {remainder_seconds} second")

""" ........................................................................"""

# Exercise 4.Consider a list of any arbitrary elements. Your code should print the length of the list and first and fourth element of the list.
elements = ["apple", "mango", "bananna", "orange", "papaya", "watermelon"]
print(f"The length of element on the list :{len(elements)}")
print(f"The first element of the list: {elements[0]}")
print(f"The fourth element of the list: {elements[3]}")


""" ........................................................................"""

# Exercise 5.Create a list of any arbitrary elements. Your code should show the list methods as pop, insert and remove.
element = ["cat", "bat", "tiger", "lion", "leopard"]

# For pop
print(element.pop())
print(f"List of element after using pop : {element}")

# For insert
element.insert(2, "hyena")
print(f"List of element after insertion of hyena in 2nd index is: {element}")

# For remove
element.remove("bat")
print(f"List of element after remove of bat is:{element}")
