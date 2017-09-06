#Inheritence
'''\
class parent():
    def f1(self):
        print("This is the parent class")


class child(parent):
    def __init__(self):
        print("This is the child class")


c = child()
#c.f2()
c.f1()
'''

# Multiple Inheritence

class mc_learning():
    def f1(self):
        print("This is machine learning ")

class web_dev():
    def __init__(self):
        print("Flask and Django are Python web frameworks")


class python(mc_learning, web_dev):
    pass

p = python()
p.f1()
#p.f2()
