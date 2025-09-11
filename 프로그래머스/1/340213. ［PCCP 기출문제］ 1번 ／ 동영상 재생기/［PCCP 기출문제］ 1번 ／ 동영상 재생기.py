# if op_start <= pos <= op_end:
#   pos = op_end
import itertools

def convert2sec(time):
    mm, ss = map(int, time.split(":") )
    return mm * 60 + ss 

def convert2time(sec):
    mm = sec // 60
    ss = sec % 60
    return f"{mm:02}:{ss:02}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = convert2sec(video_len)
    pos = convert2sec(pos)
    op_start = convert2sec(op_start)
    op_end = convert2sec(op_end)
    
    for cmd in commands:
        # 시작시 오프닝 시간에 걸릴 경우
        if op_start <= pos <= op_end:
            pos = op_end
        if cmd == "prev":
            pos = max(0, pos - 10) # 이전 했는데 -값일 경우 0으로 가야하니
        elif cmd == "next":
            pos = min(video_len, pos + 10) # 동영상 전체 길이보다 작아햐 10초 앞으로 가능
        
        # command 입력 후에도 오프닝 시간에 걸릴 경우
        if op_start <= pos <= op_end:
            pos = op_end

    return convert2time(pos)