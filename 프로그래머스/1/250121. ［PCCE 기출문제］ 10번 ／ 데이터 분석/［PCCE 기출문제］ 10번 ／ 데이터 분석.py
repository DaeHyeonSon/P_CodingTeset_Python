def solution(data, ext, val_ext, sort_by):
    
    # 컬럼명을 인덱스로 변환
    column_map = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    
    ext_idx = column_map[ext]
    sort_idx = column_map[sort_by]
    
    filtered_data = []
    
    for row in data:
        if row[ext_idx] < val_ext:
            filtered_data.append(row)
    
    
    sorted_data = sorted(filtered_data, key = lambda x: x[sort_idx])
    
    return sorted_data