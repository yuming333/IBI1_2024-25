import re

def count_tata_boxes(sequence):
    """Count the number of TATA boxes in a sequence (case-insensitive)."""
    return len(re.findall(r'TATA[AT]A[AT][AG]', sequence, re.IGNORECASE))

def process_genes(splice_combination):
    input_filename = r'C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical7/tata_genes.fa'

    output_filename = f'{splice_combination}'
    
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        current_gene = None
        current_sequence = []
        
        for line in infile:
            if line.startswith('>'):
                # If we have a gene being processed, check it before starting a new one
                if current_gene is not None and current_sequence:
                    full_sequence = ''.join(current_sequence)
                    tata_count = count_tata_boxes(full_sequence)
                    if tata_count > 0:
                        # Write to output file in the required format
                        outfile.write(f'>{current_gene} {tata_count}\n')
                        outfile.write(f'{full_sequence}\n')
                
                # Start new gene
                current_gene = line[1:].strip().split()[0]  # Get just the gene name
                current_sequence = []
            else:
                current_sequence.append(line.strip())
        
        # Process the last gene in the file
        if current_gene is not None and current_sequence:
            full_sequence = ''.join(current_sequence)
            tata_count = count_tata_boxes(full_sequence)
            if tata_count > 0:
                outfile.write(f'>{current_gene} {tata_count}\n')
                outfile.write(f'{full_sequence}\n')

def main():
    valid_combinations = ['GTAG', 'GCAG', 'ATAC']
    while True:
        splice_combination = input(f"Enter one of the splice combinations {valid_combinations}: ").upper()
        if splice_combination in valid_combinations:
            break
        print("Invalid combination. Please try again.")
    
    process_genes(splice_combination)
    print(f"Output written to {splice_combination}_spliced_genes.fa")

if __name__ == "__main__":
    main()