import os
import subprocess
import argparse

def process_file(txt_file, genome_file):
    # 获取文件名（不包括扩展名）
    base_name = os.path.splitext(os.path.basename(txt_file))[0]
    
    # 定义输出文件名
    output_file = f"{base_name}.pep.fasta"
    
    # 构建seqtk命令
    command = f"seqtk subseq {genome_file} {txt_file} > {output_file}"
    
    # 执行命令
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a txt file and run seqtk subseq.')
    parser.add_argument('txt_file', type=str, help='Path to the txt file')
    parser.add_argument('genome_file', type=str, help='Path to the genome file')
    args = parser.parse_args()
    
    process_file(args.txt_file, args.genome_file)
