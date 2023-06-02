#Pfam HMM combinations of each protein sequence across all species were used as index, and sequences with exactly the same component were write into a line.
import os

def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def write_into_dir(dict,file):
    with open(file,'r') as f2:

        for line2 in f2:
            seq = []
            id = line2.split('\t')[2].strip()
            str =line2.split('\t')[0].strip()
            seq.append(str)
            if id not in dict:
                dict[id] = seq
            else:
                dict[id] += seq

def main():
    dir='position to your pfamscan results for each species'
    id_pfam =dir+'pfam_key/'
    dir_result=dir+'domain_group_member/'
    mkdir(dir_result)
    os.chdir(id_pfam)
    dict = {}
    for file in os.listdir(id_pfam):
        if os.path.isfile(file) and file.endswith('_pfamscanid_key.txt'):
            print(file)
            write_into_dir(dict,file)
    n=1
    with open(dir_result+'pfam_final.txt','w') as f5:#输出文件
        for id,seq in dict.items():
            seq1 = [str(i) for i in seq]
            seq2 = list(set(seq1))
            seq2.sort(key=seq1.index)
            seq2 = ','.join(seq2)
            
            print('pfam|combination_' + str(n) + '|' + '\t' + '###domain_component' + '\t' + id + '\t' + '###species_identity' + '\t' + seq2,
                  file=f5)
            n+=1

main()
print('finish')