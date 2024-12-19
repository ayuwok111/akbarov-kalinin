roads = int(input())
bestroad = 0
max_height = 0
for road_number in range(1, roads + 1):
    tunnels = int(input())
    min_height = float('inf')
    for _ in range(tunnels):
        height = int(input())
        if height < min_height: 
            min_height = height
    if min_height > max_height:
        max_height = min_height
        bestroad = road_number
print(bestroad, max_height)
