#gene id of each species were used as index and the Pfam HMM component of in each sequence was integrated, eventually one file corresponds to one species and each line represents a combination of Pfam HMM in a sequence.

import os
import re
def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def write_into_dir(file,dir_result):
    dict = {}
    name=file.split('.txt')[0]
    with open(file,'r') as f3:
        for line1 in f3:
            if line1.isspace() or line1.startswith('#'):
                continue
            else:
                seq=[]
                id=re.split(r'\s+', line1)[0]
                str1='-'.join(re.split(r'\s+', line1)[5:8])
                seq.append(str1)
                if id not in dict:
                    dict[id] = seq
                else:
                    dict[id] += seq


    with open(dir_result+name+'id_key.txt','w') as f5:
        for id,seq in dict.items():
            seq1 = [str(i) for i in seq]
            seq2 = list(set(seq1))
            seq2.sort(reverse=False)
            seq2 = ';'.join(seq2)

            print( id + '\t' + '###domain_component' + '\t' + seq2, file=f5)

def main():
    dir='position of your pfamscan result files for each species'
    dir_result=dir+'pfam_key/'
    mkdir(dir_result)
    os.chdir(dir)
    for file in os.listdir(dir):
        if os.path.isfile(file) and file.endswith('_pfamscan.txt'):
            print(file)
            write_into_dir(file,dir_result)


main()
print('finish')