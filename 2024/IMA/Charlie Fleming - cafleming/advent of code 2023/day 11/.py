a = 1066
b = 1976
c = 7
d = 1918
e = 1789
f = 2.54
g = 1991
h = 96
i = 86400

result = 0

if a < i:
    result += 10    

if b * c < 16777216:
    result *= 2

if h + b < a - b + i:
    result += 200

if g < e + 20:
    result *= a

if d * 10 > c:
    result -= 250

if f < c + i * 2:
    result += 42

if a + b + c + d <= e + f + g + h:
    result /= i

print(result)