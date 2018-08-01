# DNA_strand("ATTGC")  # return "TAACG"
# DNA_strand("GTAT")  # "CATA"

# A-T; C-G
def DNA_strand(dna):
    # result = ''
    dna_reference = {
        "A": "T",
        "C": "G",
        "T": "A",
        "G": "C"
    }
    return ''.join([dna_reference[letter] for letter in dna.upper()])
    # for letter in dna.upper():
    #     result += dna_reference[letter]
    # return result


#print([dna_reference[letter] for letter in 'ttaac'])





print(DNA_strand("ATGCT"))
print(DNA_strand("cTaG"))
print(DNA_strand("ggccaT"))
print(DNA_strand("gtAt"))

