dayup,dayfactar=1,0.01
for i in range(365):
    if i%10 in[3,4,5,6]:
        dayup=dayup*(1+dayfactar)
    else:
        dayup=dayup
print("每10天休息一天：{:.2f}".format(dayup))
