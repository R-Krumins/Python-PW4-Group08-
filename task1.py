data = open('mbox-short.txt').readlines()
senders = []

for line in data:
    if line.startswith('From '):
        senders.append(line.split(' ')[1])

for s in sorted(senders): print(s)
print('Total:',len(senders))