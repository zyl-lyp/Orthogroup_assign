import os
import glob
import subprocess
import argparse

def process_domtblout_files(input_directory, output_directory):
    # 确保输出目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # 搜索目录下所有的 .domtblout 文件
    search_path = os.path.join(input_directory, '*.domtblout')
    domtblout_files = glob.glob(search_path)
    
    for file_path in domtblout_files:
        # 从文件路径中提取文件名，去除后缀
        file_name = os.path.basename(file_path).replace('.domtblout', '')
        
        # 构造输出文件名
        output_file_path = os.path.join(output_directory, f'{file_name}_out.id')
        
        # 构建并执行awk命令
        command = f"awk '{{print $1}}' {file_path} | sort -u > {output_file_path}"
        subprocess.run(command, shell=True)
        print(f'Processed {file_path} and saved output to {output_file_path}')

if __name__ == '__main__':
    # Setup argparse for command line arguments
    parser = argparse.ArgumentParser(description="Process .domtblout files and extract unique sorted IDs.")
    parser.add_argument('input_directory', type=str, help="The directory containing .domtblout files to process.")
    parser.add_argument('output_directory', type=str, help="The directory to save the output files.")
    args = parser.parse_args()

    # Run the function with the provided arguments
    process_domtblout_files(args.input_directory, args.output_directory)
