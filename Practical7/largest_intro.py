# Import neccessary libraries
import re
# Define the variable seq
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intro_seqs = re.findall(r'GT.*AG',seq) # Extract the specific intron sequence from seq

longest_seq = max(intro_seqs, key=len) # Compare the length of the elements in the intro_seqs list, and choose the longest one
max_length = len(longest_seq) # Calculate the length
print(f"The longest intron sequence is '{longest_seq}', whose length is {max_length}.") # Use f-string to print the results as a sentence, inserting the variable into the strings while avoiding making grammar mistakes