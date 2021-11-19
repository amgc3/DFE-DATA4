fin = open('zen_of_python.txt')
lines = fin.readlines()
fin.close()

fout = open('newfile.txt', 'w')

fout.writelines(lines)
fout.close()