import argparse
import time

from Ex1 import run_exercise_1
from Ex2 import run_exercise_2
from file_helper import file_param_to_file_name, generate_output_path, generate_report_path
from constants import ORFS_FILE_SUFFIX, FASTA_EXTENSION, CORRECT_ORF_FILE_SUFFIX


def main():
    # Get the current time for the output files
    str_time = time.strftime("%Y%m%d-%H%M%S");

    # Parse arguments
    parser = argparse.ArgumentParser(description="Bioinformatics Sequencing")

    # Add arguments
    parser.add_argument('-e', '--exercise', required=True)   # Ejercicio para correr
    parser.add_argument('-gb', '--genbank', help='identifier of genbank input file',
                        type=str, required=False)
    parser.add_argument('-db', '--database', help='database to use for remote consults (swissprot or nr)',
                        type=str, default='swissprot', required=False)
    parser.add_argument('-q', '--query', help='Identifier of fasta file to query',
                        type=str, required=False)
    parser.add_argument('-l', '--local', action='store_true')
    parser.add_argument('-r', '--report', help='Report output file',
                        type=str, default='myblast', required=False)
    
    args = parser.parse_args()

    input_file = ""
    output_file = ""
    database = ""
    item = 0

    # Param parsing and setup
    try:
        item = int(args.exercise)
        if args.genbank != None:
            input_file = file_param_to_file_name(str(args.genbank))
            output_file = generate_output_path(str(args.genbank))

        elif args.query != None:
            input_file = file_param_to_file_name(str(args.query))
            output_file = generate_report_path(str(args.report))
            database = str(args.database)
            if not database in ["swissprot", "nr"]:
                print("[ERROR] Invalid database option. Must be swissprot or nr.")
                exit(0)
    
    except:
        print("[ERROR] Invalid option input. Check the manual.")
        exit(0)

    # Run the exercise with the parsed params
    print("[INFO] Running exercise", item, "...")
    try:
        if item == 1:
            nucleotide_file = output_file + '_nucleotides' + FASTA_EXTENSION
            proteins_file = output_file + ORFS_FILE_SUFFIX + FASTA_EXTENSION
            final_protein_file = output_file + CORRECT_ORF_FILE_SUFFIX + FASTA_EXTENSION
            run_exercise_1(input_file, nucleotide_file, proteins_file, final_protein_file)
        
        elif item == 2:
            run_exercise_2(input_file, output_file, bool(args.local), database)
    except:
        print("[ERROR] Unknown error when running the exercise.")
        exit(0)

if __name__ == '__main__':
    main()
