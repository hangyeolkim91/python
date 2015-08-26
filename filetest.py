s = '''
 베토벤은
바이올린 선생님께
"작곡가 자질이 없다"
는 평가를 받았습니다.

엔리코 카루소는
성악 선생님으로부터
"음악에 소질이 없으니
다른 일을 하라"는 평가를
받았습니다.

학창시절 에디슨은
"지능이 모자라 교육하기
어렵다"는 평가를
받았습니다.

월트 디즈니는
"아이디어가 부족한 사람"
이라는 평가를 받고
신문사에서 쫓겨났습니다.

하지만...,
이들에 대한 평가는
틀렸습니다.

베토벤은
불후의 명곡들을 남긴
작곡가가 됐고,

엔리코 카루소는
20세기 최고의 성악가로
인정받았으며,

에디슨은
세상을 바꾼 발명왕이
됐고,

월트 디즈니는
세계적인 만화영화
제작자가 됐습니다.

사람들의 평가에
주눅들지 마세요.

그들의 평가는
절대적인 것이 아닙니다.

자신의 꿈과
믿음을 포기하지 마세요
'''
f = open('t.txt','w')
print(f)
f.write(s)
f.close()


lines = ['first line\n','seconde line\n', 'third line\n']
f = open('t3.txt','w')
f.writelines(lines)
f.close()

f = open('t4.txt','w')
f. write(''.join(lines))
#f.write(lines) lines가 문자열이 아니다
f.close()

f= open('t5.txt','w')
f.write('\n'.join(lines))
f.close()

with open('t.txt') as f:
    for line in f:
        print(line, end='')



f = open('t.txt', 'wb+')
s = b'0123456789abcdef'
print(s)
f.write(s)
f.close()