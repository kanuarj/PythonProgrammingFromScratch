'''\
def name_of_the_function():
    pass

def addition(x, y):
    z = x + y
    print(z)

addition(10, 20)
'''
'''
def func(*x, **y):
    print(x, y)


func('python', name = "Raunak")
'''
'''
def write():
    print("My name is Raunak.")

write()
write()
write()
write()
write()
'''

def dollars_to_inr(dollars=int(input("Enter the number of dollars"))):
    inr = 64.08
    while inr is 64.08:
        inr *= dollars
        print("The current rate of inr w.r.t dollars is",inr)
        break

dollars_to_inr()
