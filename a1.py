from math import *

x0 = 2.5
df = lambda x: 2*cos(x) - x/5
t = 0.01
epsilon_ = 0.000001

count = 0
max_count = 10000
step_size = 1

x_prev = x0

while count < max_count and step_size > epsilon_:
    
    delta_x = (df(x_prev))
    x_new  = x_prev + t*delta_x
    step_size = abs(x_new - x_prev)
    x_prev = x_new
    count += 1
    #print(count," ", step_size, " ", x_new)

print("The optimum is %s after %s iterations." %(x_new, count))


f0 = (-1,1)
dfdx = lambda x,y: 2*y + 2 - 2*x
dfdy = lambda x,y: 2*x - 4*y

t = 0.01
epsilon_ = 0.000001

count = 0
max_count = 10000
step_size = 1

f_prev = f0

while count < max_count and step_size > epsilon_:
    
    delta_f = (dfdx(f_prev[0],f_prev[1]),dfdy(f_prev[0],f_prev[1]))
    #print(delta_f)
    f_new  = (f_prev[0]+t*delta_f[0],f_prev[1]+t*delta_f[1])
    
    step_size = sqrt((f_new[0]-f_prev[0])**2 + (f_new[1]-f_prev[1])**2)
    
    f_prev = f_new
    count += 1
    #print(count," ", step_size, " ", f_new)

print("The optimum is %s after %s iterations." %(f_new, count))
