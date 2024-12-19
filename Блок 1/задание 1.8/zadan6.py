def find_cattle_combinations(total_money, total_heads):
    results = []
    
    for bulls in range(1, total_money // 20 + 1):
        remaining_money = total_money - bulls * 20
        remaining_heads = total_heads - bulls
        
        for cows in range(remaining_heads + 1):
            calves = remaining_heads - cows
            
            if (cows * 10 + calves * 5) == remaining_money:
                results.append((bulls, cows, calves))
    
    return results

total_money = int(input().strip())
total_heads = int(input().strip())

combinations = find_cattle_combinations(total_money, total_heads)

for bulls, cows, calves in combinations:
    print(bulls, cows, calves)
