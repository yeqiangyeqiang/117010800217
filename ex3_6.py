import time
scale = 10
t = time.clock()
for i in range(scale + 1):
    a = '.' * i
    print("\rStarting [{}] Done".format(a),'')
    time.sleep(0.1)
