fin = open('dog_breeds.txt')
#read all the lines of the text file and return them as a list of strings.
lines = fin.readlines()
#['Pug\n', 'Jack Russell Terrier\n', 'English Springer Spaniel\n', 
# 'German Shepherd\n', 'Staffordshire Bull Terrier\n', 'Cavalier King Charles Spaniel\n',
#  'Golden Retriever\n', 'West Highland White Terrier\n', 'Boxer\n', 'Border Terrier']
for line in lines:
    print(line.strip())  # removes whitespace, newlines and print