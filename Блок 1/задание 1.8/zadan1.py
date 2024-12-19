columns = int(input())
rows = int(input())
for row in range(1, rows + 1):
        rowv = []
        for col in range(1, columns + 1):
            value = col / row
            rowv.append(f"{value:.1f}") 
        print(" ".join(rowv))
    
