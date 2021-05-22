f = 10
r = 10.5
j = 13.7
if r > j:
    print("r > j")
elif r < j:
    print("r < j")
else:
    print("r == j")



g = 2**3
q = 3**2
if g > q:
    print(g)
else:
    print(q)


s = -50
if (s > 0 and s < 22) or (s > 56 and s < 100):
    print('разрешенное')
else:
    print('запрещенное')

    
k = 29
if (k / 2):
    print('четное')
else:
    print('не четное')
if (k / 3):
    print('true')
else:
    print('folse')
if (k ** 2 > 1000):
    print('true')
else:
    print('folse')


print('helo world')


a = 10 // 5
b = 10 / 5
c = a + b
if a == b:
    print(c)

l = -1
if(l < 0):
    print(l)
else:
    print('folse')


u = 10
p = -6
if (u and p) > 0:
    print('true')
else:
    print('folse')
if u > p:
    print(u + 2)
else:
    print(p + 2)


z = int(input('введите число'))
if (z > 0):
    print('положительное число')
else:
    print('отрицательное число')


w = int(input('сколько тебе лет'))
if w > 18:
    print('ты большой')
if w < 18 and w > 14:
    print('подросток')
else:
    print('ребёнок')


n = 45
t = 6
m = n / t
if m / 2:
    print('делится')
else:
    print('не делится')


p = int(input('введите год'))
if p < 2021:
    print('этот год прошол')
elif p > 2021:
    print('этот год ещё не наступил')
else:
    print('это тикущий год')



a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
if a < b and a < b:
    print(a)
elif b < c and b < a:
    print(b)
else:
    print(c)


x = 13
z = 13 ** 2
if z > 172:
    print(z)
elif z < 172:
    s = (z ** 2)
    print(s)
