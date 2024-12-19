def dance_counting():
    import sys

    n = int(input().strip())
    
    expected_counts = ["раз", "два", "три", "четыре"]
    
    correct_count = 0  
    error_count = 0   

    while True:
        try:
            count = input().strip()
        except EOFError:
            break 
        
        expected_index = correct_count % 4
        
        if count == expected_counts[expected_index]:
            correct_count += 1 
        else:
            error_count += 1  
            print(f"Правильных отсчётов было {correct_count}, но теперь вы ошиблись.")
            correct_count = 0  
            
            if error_count >= n:
                print("На сегодня хватит.")
                break 

dance_counting()
