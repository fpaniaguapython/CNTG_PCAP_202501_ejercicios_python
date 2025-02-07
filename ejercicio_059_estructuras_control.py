edad = 20
if edad<20:
    pass
elif edad==20:
    pass
elif edad<30:
    pass
else:
    pass

match edad:
    case 18:
        print(18)
    case 20:
        print(20)
    case 30:
        print(30)
    case _:
        print('No sé')

while(edad<100):
    edad+=1

for i in range(100): # Este range va entre 0 y 99 
    if i>95: print(i)

