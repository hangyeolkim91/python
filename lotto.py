#국민대학교 20113274 김한결
# 로또 번호 생성기

import random

s = set()

times = 50

while  times:

    while s.__len__() <6: #집합의 원소가 6개가 될때까지 반복
        s.add(random.randrange(1,47))

    print(s)
    s.clear()
    times -=1