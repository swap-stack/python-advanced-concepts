def my_funct(arg=42):
    """

    Placeholder function

    """
    print('Printing the function\'s argument')

print(my_funct)

new_funct = my_funct
new_funct()

print(new_funct.__doc__)
print(new_funct.__name__)
print(new_funct.__defaults__)

functs = [str.lower, print, range]

for f in functs:
    print(f"The function name is \"{f.__name__}\"")

print(functs[0]('PYTHON'))

#Closures

def foo():
    x = 42

    def bar():
        print(x)

    return bar

var = foo()

