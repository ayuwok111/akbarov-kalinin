line_number = 0

while True:
    line = input()
    line_number += 1 

    if line == "СТОП":
        print(-1) 
        break

    if 'кот' in line.lower():
        print(line_number) 
        break
