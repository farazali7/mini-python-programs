DNAstring = "GTCGCCGTACTATGGTCGGTACACCGACCGGGCCTGCAATCACGGGTGGGGCAAGTTGTCCATATATTCCCCAACAGTACGTCGATGTGGAGTAGACTCGGTTTGACTTCCACTGGTAACTCAAATCGCTACCCTAGGCCTACATGAGCTACGCAAGGAGCATAGGCACCAACGGCCAGGTTGCCGAATGAAGGTATAAGAGTTGACAAAGGAGCACGTTAAGTGAAGTGTGGTTGCGTAGAGACTTGTGGATTTGCAATGAGCGGGACGACTGAAGGCCCAGGTCGCTGTATATGAGCGGCCTGAGGGTGGGTAAGTCGCCTATTAATCTTGGAGCCGAGCTCCCCAGAAGTAAAATAGTGTCGTTCGTAACCGTCAAAGATGACACCGCTCTACATGGTTTAAAGCGACTGAGGGTCGGGCTAACGTTCGCCATGACCGATATGCTCGTCTGGAGTAAGTAAGTCGTTCGCACAACCAAGCTGAGCTATGAGAGTCCTGGATCAACTGATGGATGAAAGACGCTTAAGAGTGATCGCTCTGACTCTGCGGACAGTTGAAGGAGGTAAGGGGCCTGGACATCCTGACGCGAGATACTAAAGGCTTTCGGCGTAGGTCACGACCCGCATCAAAAGGTCCTCACTCCACACGATCTCCGTGAGCCGGGGTCAAGCTCGCTCTGCTCAAAGTCACACGAAAATGCGGGAACGCCGCAAAGTCTCCGGGCAAGTGGAGGGTAGTACGTTCAACTTTTAATGAACGCTGGATCCTAGGAGCGTCGCCAATGCCATCCTGAGGTTAACCCCCACACTTACTCATGGACGTTTACTCTTGACAGCGAAGTTGGAACATGCGAGTAGACGAAAAGTGACTGTCCGGAGTGCGGGGAGGATGGGGAATCATCGCTTTTGGGGACAAACCAATCCGCCCGGGTATACAATTATAACTATGGCCTGTTTCCTCGAGCAGG"
def RNATRANSLATE(string):
    RNAstring = ''
    for i in range(len(string)):
        if string[i] is 'T':
            RNAstring = RNAstring + 'U'
        else:
            RNAstring = RNAstring + string[i]

    print(RNAstring)


RNATRANSLATE(DNAstring)
