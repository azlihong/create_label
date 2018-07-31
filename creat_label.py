import os
rootdir = 'images1'
list = os.listdir(rootdir)
for i in range(0,len(list)):

        print list[i]
        f = open('images1.txt', 'a')
        #f.write(list[i]+'\n')
        f.write(list[i]+' '+'0'+'\n')
        f.close()

