def main(n):
    is_chet = [True] * n
    is_chet[0] = is_chet[1] = False  
    for i in range(2, int(n**0.5) + 1):
        if is_chet[i]:
            for j in range(i * i, n, i):
                is_chet[j] = False
    return [i for i in range(n) if is_chet[i]]
n = int(input())
chet = main(n)
for chet in chet:
    print(chet)
