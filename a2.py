from math import *

x0 = 2.5
df = lambda x: 2*cos(x) - x/5
d2f = lambda x: -2*sin(x) - 1/5

count = 0
max_count = 10000
epsilon_ = 0.000001
step_size = 1

prev_x = x0
while count < max_count and step_size > epsilon_:

    v = -(1/d2f(prev_x))*(df(prev_x))
    new_x = prev_x + v

    step_size = new_x - prev_x
    count += 1
    prev_x = new_x

print("The result is %s after %s iterations."%(new_x,count))


def dx(f, x):
    return abs(0-f(x))
 
def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
        print ('Root is at: ', x0)
        print ('f(x) at root is: ', f(x0))





def f(x):
    return 2*sin(x)*(x**2)/10
 
def df(x):
    return 2*cos(x)-x/5


newtons_method(f, df, x0, 1e-5)
