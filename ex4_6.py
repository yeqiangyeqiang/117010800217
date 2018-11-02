import random
a=['羊1','羊2','汽车']
first_guess_count=0
change_guess_count=0
for i in range(100000):
    guess=random.choice(a)
    if guess=='汽车':
        first_guess_count+=1
    else:
        change_guess_count+=1
print("改变选择获胜概率：{:.4f}:坚持选择获胜的概率：{:.4f}".format(first_guess_count/100000,change_guess_count/100000))
