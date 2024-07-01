import os
import sys

def process_blast_output(file_path, output_dir):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            key = parts[0]  # First column as the key
            if key in data:
                data[key].append(line)
            else:
                data[key] = [line]

    # Creating the specified output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Writing each grouped lines to separate files based on the first column
    for key, lines in data.items():
        with open(os.path.join(output_dir, f'{key}.blastout'), 'w') as output_file:
            output_file.writelines(lines)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_directory>")
        sys.exit(1)
    file_path = sys.argv[1]
    output_dir = sys.argv[2]
    process_blast_output(file_path, output_dir)

