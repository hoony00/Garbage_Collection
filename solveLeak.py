# Leak.py에서 Memory leak를 일으키는 경우와 해결법
import time

class MyObject:
    def __init__(self):
        self.data = [1] * 10

def run():
    objs = []
    for i in range(10):
        objs.append(MyObject())
        time.sleep(0.1)
#★ gc.collect() 사용 대신 del objs를 사용해서 호출 비용을 줄임 
# > gc는 현재의 객체들이 참조하는 다른 객체들의 참조 카운트도 함께 검사되므로, 호출 비용이 더 많이 들어감
# >  파이썬은 메모리가 부족한 경우에 자동으로 gc가 수행되기도 함
    del objs      # > objs 리스트를 삭제하여 Memory leak를 방지합니다.
