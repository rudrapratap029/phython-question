# 4. Function with Default Parameter

def greet_user(name="Guest"):
    print("Welcome,", name)

greet_user()
greet_user("Rudra")


# 5. Function with Multiple Returns
def calculate(a, b):
    return a + b, a - b

sum_result, diff_result = calculate(10, 4)
print("Sum:", sum_result)
print("Difference:", diff_result)

# 6. Function Calling Another Function

def square(x):
    return x * x

def cube(x):
    return x * x * x

num = 3
print("Square:", square(num))
print("Cube:", cube(num))

