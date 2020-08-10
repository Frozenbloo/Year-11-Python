import time
'''
for x in range (5000):
    wait
    print(x)
'''
'''
for x in range (0,10):
    print("Hello World")
    print("I Love Python")
print("I Need Sleep")
'''
'''
for x in range (5):
    print("This Is Iteration:", x)
'''

for x in range (10,1,-1):
    time.sleep(1)
    print(x)

for x in range (1,3):
    print("This is OUTER Loop statement ", x)
    for y in range(1,4):
        print("This is INNER Loop Statement - - ", y)

for x in range (1,3):
    print("This is OUTER Loop statement ", x)
    for y in range(1,4):
        print("This is INNER Loop Statement - - ", y)
        for z in range(1,5):
            print("This Is Second INNER Loop Statement - - - - ", z)

for x in range (1,4):
    print("This Is INNER Loop Statement ", x)
    for y in range (1,3):
        print("This Is INNER Loop Statement ", x ,"," , y)
    
for x in range (50):
    print("============= RESTART: S:/Year 11/Python Yr11/Simple For Loop.py =============")

for x in range (50):
    print(x * "*")

for x in range (50,0,-1):
    print(x * "*")


