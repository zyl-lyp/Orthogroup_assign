import sys
import glob
import os

def extract_orthogroups(protein_id_files, orthogroups_file, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each protein ID file
    for protein_id_file in protein_id_files:
        # Read protein IDs
        with open(protein_id_file, 'r') as file:
            protein_ids = {line.strip() for line in file}

        # Read Orthogroups file and match IDs
        matched_lines = []
        with open(orthogroups_file, 'r') as file:
            for line in file:
                if any(protein_id in line for protein_id in protein_ids):
                    matched_lines.append(line)

        # Construct output file path
        output_file_path = os.path.join(output_folder, os.path.basename(protein_id_file) + '.filter.id')

        # Write matched lines to a new file
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(matched_lines)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_directory_with_id_files> <orthogroups_file> <output_folder>")
        sys.exit(1)

    input_directory = sys.argv[1]
    orthogroups_file = sys.argv[2]
    output_folder = sys.argv[3]

    # Find all .id files in the input directory
    protein_id_files = glob.glob(os.path.join(input_directory, '*.id'))
    
    # Execute the function
    extract_orthogroups(protein_id_files, orthogroups_file, output_folder)
