import sys

def extract_orthogroups(protein_id_file, orthogroups_file, output_file):
    # Reading protein IDs
    with open(protein_id_file, 'r') as file:
        protein_ids = {line.strip() for line in file}

    # Reading Orthogroups file and matching IDs
    matched_lines = []
    with open(orthogroups_file, 'r') as file:
        for line in file:
            # Check if any protein ID is contained in the line
            if any(protein_id in line for protein_id in protein_ids):
                matched_lines.append(line)

    # Writing matched lines to a new file
    with open(output_file, 'w') as file:
        file.writelines(matched_lines)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <protein_id_file> <orthogroups_file> <output_file>")
        sys.exit(1)

    protein_id_file = sys.argv[1]
    orthogroups_file = sys.argv[2]
    output_file = sys.argv[3]

    # Execute the function with command-line provided file paths
    extract_orthogroups(protein_id_file, orthogroups_file, output_file)

