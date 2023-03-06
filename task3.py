import re

def getLetterFrequency(file):
    #extract all letters from file
    data = re.findall('[a-z]', open(file).read().lower())
    
    #count frequency of letters, put result in a dictionary
    letters = dict()
    for l in data:
        if l not in letters: letters[l] = 1    
        else: letters[l] += 1
    
    #compute letter count as percantage of total and sort in decreesing order, put result in a dictionary
    letters_processed = dict()
    for k,v in sorted(letters.items(), key=lambda i:i[1], reverse=True):
        letters_processed[k] = '{:.1f}'.format((v/len(data)*100))

    return letters_processed



letters = getLetterFrequency('bee-movie-script.txt')
      
for k,v in letters.items():
    print('{}: {}%'.format(k, v))


