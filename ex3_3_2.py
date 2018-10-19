dayup,dayfactar,dayupa=1,0.01,1
for i in range(365):
    if i%15 in[3,4,5,611,12,13,14]:
        dayup=dayup*(1+dayfactar)
    else:
        dayup=dayup
print("连续努力365天：{:.2f}".format(dayup))
