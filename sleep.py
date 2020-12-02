import time as t

u = "Hello, Patrick :)"
k = 0

while k < len(u):
    t.sleep(.25)
    print(u[k], end="")  # This end argument forces print() to stay on the same line.
    k += 1
print("")
t.sleep(1.)
