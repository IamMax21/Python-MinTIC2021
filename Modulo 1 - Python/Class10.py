#Iteradores


1 in range(1,4)
#True

for i in range(1, 4):
    print(i)
#1
#2
#3

for i in ["max", "jimenez", True, 2.34]:
    print(i)
#max
#jimenez
#True
#2.34

for i in ["max", "jimenez", True, 2.34]:
    if i=="max":
        print("Si esta Max")
#max
#jimenez
#True
#2.34
"""
Con los iteradores podemos hacer muchisimas condicionales de manera repetitiva de manera automatica.
"""