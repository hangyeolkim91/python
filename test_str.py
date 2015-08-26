__author__ = 'user'
multiline = '''
I'm gona kill you
really
really
'''

print(multiline.__repr__())
print(multiline)
print(type(multiline))

print(format(123456789, ',d'))
print(format(123456789.23213123,',.2f'))

D = {'name':'박성범','age':'24'}
birth_msg = '''
안녕하세요 {name} 님. {age}살 생일을 축하합니다.
'''
print(birth_msg.format_map(D))

print('{0:b} {0:d} {0:o} {0:x} {0:X} {1:d} {1:n}'.format(13,123456789))
print('{0:010x}'.format(123))

s = '성범아 뭐하니 던파요'

print(s.strip())

t = s.split()
print(t)

print(s.rjust(30,'='))

print('x'.join(t))