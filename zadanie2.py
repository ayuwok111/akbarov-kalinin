n = int(input())

found = False

for _ in range(n):
    line = input() 
    if 'кот' in line.lower(): 
        found = True
        break

if found:
    print("МЯУ")
else:
    print("НЕТ")
