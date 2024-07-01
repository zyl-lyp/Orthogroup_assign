def clean_fasta(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()
        write_line = False
        for line in lines:
            if line.startswith(">"):
                if write_line:  # Only write the previous header if it had sequence data
                    outfile.write(header + sequence + '\n')
                header = line
                sequence = ''
                write_line = False
            else:
                sequence += line.strip()
                if sequence:
                    write_line = True
        if write_line:  # Write the last sequence if it had sequence data
            outfile.write(header + sequence + '\n')

input_file = 'IG_allgenome.fa'
output_file = 'IG_allgenome_cleaned.fa'
clean_fasta(input_file, output_file)
