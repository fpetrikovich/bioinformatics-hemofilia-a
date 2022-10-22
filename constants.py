from enum import Enum

FASTA_EXTENSION = ".fasta"
FASTA_TYPES = ['fas', 'fasta', 'faa']
OUTPUT_TYPES = ['txt', 'output', 'out']
ORFS_FILE_SUFFIX = "_proteins"
CORRECT_ORF_FILE_SUFFIX = "_final_protein"

START_CODON = "AUG"
END_CODONS = ["UAA", "UAG", "UGA"]

# mRNA coagulation factor VIII GenBank Files
class mRNA_GENBANK_FILES(Enum):
    ISOFORM_A_PREPROTEIN = "GenBank_F8_mRNA/NM_000132.4_sequence.gb"
    ISOFORM_B = "GenBank_F8_mRNA/NM_019863.3_sequence.gb"

class FASTA_FILES(Enum):
    ORFS_ISOFORM_A_PREPROTEIN = "1A" + ORFS_FILE_SUFFIX + FASTA_EXTENSION
    ORFS_ISOFORM_B = "1B" + ORFS_FILE_SUFFIX + FASTA_EXTENSION
    ISOFORM_A_PREPROTEIN = "1A" + CORRECT_ORF_FILE_SUFFIX + FASTA_EXTENSION
    ISOFORM_B = "1B" + CORRECT_ORF_FILE_SUFFIX + FASTA_EXTENSION
