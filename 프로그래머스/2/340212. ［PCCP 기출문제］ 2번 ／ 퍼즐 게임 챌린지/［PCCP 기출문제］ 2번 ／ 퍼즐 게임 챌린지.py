# 이분탐색
def solve_simulation(diffs, times, limit, level):
    
    n = len(diffs)
    
    puzzle_time = 0
    
    for i in range(n):
        diff = diffs[i]
        time_cur = times[i]
        time_prev = times[i-1]
        
        if level >= diff:
            puzzle_time += time_cur
        else: 
            failed_solve = diff - level
            
            solved_time = time_cur * failed_solve
            solved_time += time_prev * failed_solve
            solved_time += time_cur
            
            puzzle_time += solved_time
            
        
        if puzzle_time > limit:
            return False
    
    return True

def solution(diffs, times, limit):
    
    low = 1
    high = max(diffs)
    
    while low <= high:
        
        mid_level = (low + high) // 2
        
        result = solve_simulation(diffs, times, limit, mid_level)
        
        if result:
            high = mid_level - 1
        else:
            low = mid_level + 1
    
    return low