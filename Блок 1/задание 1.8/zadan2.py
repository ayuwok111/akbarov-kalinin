def draw_rectangle():
    import sys
    
    height = int(sys.stdin.readline().strip())
    width = int(sys.stdin.readline().strip())
    symb = sys.stdin.readline().strip()
    
    first_last_row = symb * width
    
    middle_row = symb + ' ' * (width - 2) + symb if width > 1 else symb

    print(first_last_row)
    for _ in range(height - 2): 
        if height > 1:
            print(middle_row)
    if height > 1: 
        print(first_last_row)

if __name__ == "__main__":
    draw_rectangle()
