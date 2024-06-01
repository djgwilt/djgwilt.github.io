num = input("Enter a number: ")
num = int(num)
double = 2 * num
treble = 3 * num

for count in range(num,treble+1,1):
    if count != double:
        print(count)