from constants import mRNA_GENBANK_FILES

input_folder = "Inputs\\"

def file_param_to_file_name(param):
    file_names = {
        "1A": mRNA_GENBANK_FILES.ISOFORM_A_PREPROTEIN.value,
        "1B": mRNA_GENBANK_FILES.ISOFORM_B.value,
    }
 
    return input_folder + file_names.get(param, "")