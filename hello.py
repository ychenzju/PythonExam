#! usr/bin/python3

def say_hello(name):
    print("Hello {name}!".format(name=name))

say_hello("Yao Chen")
print('Testing...')

for n in range(10):
    print('{0} * {1} = {2}'.format(n,n,n**n))

