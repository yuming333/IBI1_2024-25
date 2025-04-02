import re
# Print file path
input_file = r'C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
out_file= r'C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical7/tata_genes.fa'

line_length = 1000000099 # Number of the bases shown in each line

# Define the regular expression of TATA box sequence
tata_pattern = re.compile(r'TATA[AT]A[AT]')

# Initialize variables to store the gene name and gene sequence
gene_name = ''
gene_seq = ''

# Open the file and write the results inside,and close automatically afterwards
with open(out_file, 'w') as output_file:
    #  Open input_file to read
    with open(input_file, 'r') as input_file:
        for line in input_file:
            if line.startswith('>'):
                # Check if previous sequence contains TATA box sequence when encountered with a new gene
                if gene_seq and tata_pattern.search(gene_seq):
                    output_file.write(f">{gene_name}\n")
                    # Write the sequence in the output_file with defined line length
                    for i in range(0, len(gene_seq), line_length):
                        output_file.write(gene_seq[i:i + line_length] + '\n')
                # Extract gene name
                gene_name = re.findall(r'gene:(.+?)\s', line)
                if gene_name:
                 gene_name = gene_name[0]
                # Clear gene_name and gene_seq
                else:
                    gene_name = ''
                gene_seq = ''
            else:
                # Connect the selected gene sequences without whitespace
                gene_seq += line.strip()
    # After this loop, the last gene sequence has been stored in the gene_seq. 
    # However, it is missed because there is no '>' to trigger its checking proccess.

    # Check if the last gene contains TATA box sequence
    if gene_seq and tata_pattern.search(gene_seq):
        output_file.write(f">{gene_name}\n")
    # Write the sequence in the output_file with defined line length
        for i in range(0, len(gene_seq), line_length):
            output_file.write(gene_seq[i:i + line_length] + '\n')











