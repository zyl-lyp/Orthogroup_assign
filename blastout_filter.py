import os
import glob
import argparse

def filter_and_sort_blastout_files(input_directory):
    # Construct the path to search for .blastout files
    search_path = os.path.join(input_directory, '*.blastout')
    blastout_files = glob.glob(search_path)
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
    # Setup argparse for command line arguments
    parser = argparse.ArgumentParser(description="Filter and sort BLAST output files based on specific criteria.")
    parser.add_argument('input_directory', type=str, help="The directory containing .blastout files to process.")
    args = parser.parse_args()

    # Run the function with the provided arguments
    filter_and_sort_blastout_files(args.input_directory)
