import os
# insert working directory here:
#os.chdir("C:\\Users\\...")

fhand = open('mbox-short.txt').readlines()

def get_email_from_str(str):
    return str.split(' ')[1].strip()

def get_domain_from_email(str):
    return str.split('@')[1].strip()

def count_domains(file = fhand):
    count_dict = dict()
    for line in file:
        if line.startswith('From'):
            email = get_email_from_str(line)
            domain = get_domain_from_email(email)
            if domain not in count_dict:
                count_dict[domain] = 1
            else:
                count_dict[domain]+= 1
    return count_dict

def display_histogram(cdict):
    for k, v in sorted(cdict.items()):
        print('{:>20}: {:>2} {}'.format(k,v,'*'*v))

print('SORTED:') 
cdict = count_domains(fhand)
display_histogram(cdict)
