import datetime
import time
import glob
filelist =glob.glob('*DATA')
filelist.append('')
indx = 0

input = open('DATA','a')

while filelist[indx]:
    with open(filelist[indx],'r') as f:
        data=f.read()

    indx+=1
    print(data)
    input.write(data)


input.close()