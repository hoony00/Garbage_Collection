# -*- coding: UTF-8 -*-
# GC 로도 Memory leak이 발생하는 경우와 제대로 동작되도록 코드를 어떻게 작성해야지 서술
import gc

class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def __str__(self):
        return f"Person({self.name})"

# 객체 리스트 생성
objects = []
for i in range(10):
    p = Person(f"person{i}")
    objects.append(p)
    if i > 0:
        objects[i-1].add_friend(p)
        p.add_friend(objects[i-1])

# 객체 리스트의 일부를 삭제합니다.
del objects[5:6]

# 가비지 컬렉션 수행    # !-- GC 가 제대로 동작되도록 코드를 어떻게 작성하는 법 --!
gc.collect()          # gc를 사용하였으나 서로가 서로를 참조하고 있기 때문에 가비지 컬렉션 알고리즘은 이 객체들을 참조하고 있는 상호 참조 그룹을 모두 살려둬야 함. 그렇기 떄문에 메모리에서 제거되지 않음. 이를 해결하기 위해서는 객체들이 서로를 참조하지 않도록 구현하는 것이 중요함. 

# 삭제된 객체들의 참조 카운트 출력
print("삭제된 객체들의 참조 카운트 출력")
for i in range(5, 6):
    print(gc.get_referrers(objects[i]))
