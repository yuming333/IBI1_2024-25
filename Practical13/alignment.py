import re # Import neccessary library
#File paths
human=r"C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical13/human.fasta.txt"
mouse=r"C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical13/mouse.fasta.txt"
random=r"C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical13/Random.fasta.txt"
blosum62=r"C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical13/BLOSUM62.txt"

def read_file(file_path):# get the sequence 
    sequence = "" # Initialize an empty string
    with open(file_path,"r")as file: 
        for line in file:
            if not re.search(r"^>", line):
                sequence += line.strip().upper() # Get the sequence lines, remove whitespace characters (including newlines), and convert all alphabetic characters to uppercase.
    return sequence
def load_blosum62(filepath): # Load the BLOSUM62 matrix from the existing file
    with open(filepath, 'r') as file:
        matrix = {} # Initialize an empty dictionary
        # Remove empty lines and comments
        lines = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        header = lines[0].split() 
        for line in lines[1:]:
            parts = line.split()# Split the lines 
            row_aa = parts[0] 
            scores = list(map(int, parts[1:]))
            # Create a dictionary: amino acids as keys and scores as values
            for col_aa, score in zip(header, scores):
                matrix[(row_aa, col_aa)] = score
    return matrix
     
def similiarity(seq1, seq2): # Calculate the similarity between two sequences
    
    similiarity_count = 0 
    scores = 0 
    for i in range(len(seq1)):
        scores += matrix.get((seq1[i], seq2[i]), -4) # Sum up the score 
        if seq1[i] == seq2[i]:
            similiarity_count += 1 # Count the number of identical amino acids
    # Calculate similarity and print results
    similiarity = similiarity_count / len(seq1)
    print(f"Similarity: {similiarity*100:.2f}%")
    print(f"Score: {scores}")

# Get matrix
matrix=load_blosum62(blosum62)
# Get length of the sequence
length_SOD2 = len(read_file(human))
# Get sequences
sequence_h= read_file(human)
sequence_m= read_file(mouse)
sequence_r= read_file(random)
# Get the scores and similarity  
similarity_hm = similiarity(sequence_h, sequence_m)# similarity between human and mouse
similarity_hr = similiarity(sequence_h, sequence_r)# similarity between human and random
similarity_mr = similiarity(sequence_m, sequence_r)# similarity between mouse and random
print(f"Length of SOD2: {length_SOD2}")




            
    
