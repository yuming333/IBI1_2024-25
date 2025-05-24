def find_restriction_sites(DNA_sequence, restriction_site):
    """
    Find all restriction enzyme cut sites in a DNA sequence.
    
    Args:
        DNA_sequence (str): DNA sequence to search
        recognition_sequence (str): Restriction enzyme recognition sequence
        
    Returns:
        list: Positions of cut sites (1-based indexing), or error message if invalid sequences
    """
    valid = {'A', 'C', 'G', 'T'}
    
    # Validate sequences
    if any(nuc.upper() not in valid for nuc in DNA_sequence):
        return "Error: DNA sequence contains invalid nucleotides (only ACGT allowed)"
    if any(nuc.upper() not in valid for nuc in restriction_site):
        return "Error: Recognition sequence contains invalid nucleotides (only ACGT allowed)"
    
    # Find all matches (1-based indexing)
    recog = restriction_site.upper()
    return [i+1 for i in range(len(DNA_sequence)-len(recog)+1) 
            if DNA_sequence.upper()[i:i+len(recog)] == recog]

DNA_sequence = input('Enter the DNA sequence: ')
restriction_site = input('Enter restriction site: ')
print(find_restriction_sites(DNA_sequence, restriction_site))

# Example usage
print(find_restriction_sites("GAATTCGCTTAAGGAATTC", "GAATTC"))  # [1, 14]
print(find_restriction_sites("GGATCCAGCTAGGATCC", "GGATCC"))    # [1, 12]
print(find_restriction_sites("ATCGATCG", "XYZ"))                 # Error
print(find_restriction_sites("ATCGNATCG", "ATCG"))               # Error