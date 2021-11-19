fin = open('dog_breeds.txt')
# use file object as part of for loop
# => we can iterate directly on fin without calling readlines()
fout = open('allupper.txt', 'w')
for line in fin:
    print(line.strip().upper())
    fout.write(line.upper())
fout.close()
fin.close()
