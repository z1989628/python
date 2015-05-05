myfile = open('test.txt')
line_pos = []

mypos = myfile.tell()
line_pos.append(mypos)
line = myfile.readline()
while line != '':
    mypos = myfile.tell()
    line_pos.append(mypos)
    line = myfile.readline()

for e in line_pos:
        print e
