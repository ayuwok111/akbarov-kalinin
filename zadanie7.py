def main():
    N=int(input())
    blocks=[int(input()) for _ in range (N)]
    hpr=0
    for i in range(N):
        bn=blocks[i]
        hn = bn % 256
        rn = (bn // 256) % 256
        mn = bn // (256 * 256)
        if hn >= 100:
            print(i)
            return
        hc=(37 * (mn + rn + hpr)) % 256
        if hn !=hc:
            print(i)
            return
        hpr = hn
    print(-1)
if __name__ == "__main__":
    main()
