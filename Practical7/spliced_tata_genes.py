
# import re
import re

# input the one	of three possible splice combinations
valid_combinations = input("please provide the valid_combinations (ATAC,GCAG,GTAG): ")

# set the input and output path and output file name
input = r'C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output = f'C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical7/{valid_combinations}_spliced_genes.fa'


# Analyze FASTA file
genes = {}
current_gene = None
with open(input, 'r') as file:
    for line in file:
        line = line.strip() # Delete white space
        
        if line.startswith('>'):
            match = re.search(r'gene:(\S+)', line)
            if match: 
                current_gene = match.group(1) 
                genes[current_gene] = "" 
    
        elif current_gene is not None: 
            genes[current_gene] += line

# Select genes that contain the specified splice site
keys_to_delete = []
for gene_name in genes:
    cut = valid_combinations[:2] + r'.*' + valid_combinations[-2:]  # pattern
    seqs = re.search(cut, genes[gene_name])
    if  not seqs:
        keys_to_delete.append(gene_name)

for key in keys_to_delete:
    del genes[key]



# get key and value, filtrate TATA
tata_genes = {}
for gene_name in genes:
    sequence = genes[gene_name]  

    if re.search(r'TATA[AT]A[AT]', sequence):
        tata_genes[gene_name] = sequence

# output the result
with open(output, 'w') as file:
    for gene_name, sequence in tata_genes.items():
        t = re.findall(r'TATA[AT]A[AT]', sequence)
        file.write('>' + gene_name + ' :' + str(len(t)) + '\n')
        file.write(sequence + '\n')