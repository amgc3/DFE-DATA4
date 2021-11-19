 fin = open('dog_breeds.txt')
# use file object as part of for loop
# => we can iterate directly on fin without calling readlines()
for line in fin:
    print(line.strip())
