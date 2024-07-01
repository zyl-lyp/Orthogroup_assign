import sys

def simplify_header(file_path, output_file_path):
    with open(file_path, 'r') as file, open(output_file_path, 'w') as output:
        for line in file:
            if line.startswith('>'):
                # Extracting the ID and simplifying it
                header = line.strip().split('|')[1]
                output.write(f'>{header}\n')  # Now correctly writes newline
            else:
                # Writing sequence lines as is
                output.write(line)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Calling the function to simplify the headers
    simplify_header(input_file, output_file)

