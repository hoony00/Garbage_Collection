# Memory leak를 일으키는 경우

import time

class MyObject:
    def __init__(self):
        self.data = [1] * 10

def run():
    objs = []
    for i in range(10):
        objs.append(MyObject())
        time.sleep(0.1)  # Memory leak를 일으키기 위해 잠시 대기 
    # 함수 종료 후 objs 리스트는 더 이상 사용되지 않으므로 제거되어야 함 ---> Memory leak 발생
    # objs 리스트와 그 안에 MyObject 인스턴스들도 Memory에서 삭제되지 않음!
    # 해결 법: objs 리스트를 전역 범위로 옮기거나 함수 내에서 명시적으로 삭제해야 함! -> solveLeak.py에서 구현
