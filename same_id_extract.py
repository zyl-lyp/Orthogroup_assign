import os
import glob

def filter_and_sort_blastout_files():
    # List all .blastout files in the current directory
    blastout_files = glob.glob('*.blastout')
    for file_path in blastout_files:
        data_set = set()  # To hold unique values
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 3 and parts[2] == '100.000':
                    data_set.add(parts[1])

        # Sort the unique values
        sorted_data = sorted(data_set)

        # Write to a new file with .filter.id
        output_file_path = file_path.replace('.blastout', '.blastout.filter.id')
        with open(output_file_path, 'w') as output_file:
            for item in sorted_data:
                output_file.write(item + '\n')

if __name__ == '__main__':
    filter_and_sort_blastout_files()
