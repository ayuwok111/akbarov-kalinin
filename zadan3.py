def countdown_launches():
    import sys
    
    n = int(sys.stdin.readline().strip())
    
    for i in range(n):
        countdown_time = i
        
        for j in range(countdown_time + 1):
            print(f"Осталось секунд: {countdown_time - j}")
        
        print(f"Пуск {i + 1}")

if __name__ == "__main__":
    countdown_launches()
