import os
import subprocess
import argparse

def process_files(input_folder, genome_file):
    # 获取输入文件夹下所有的txt文件
    txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    # 循环处理每一个txt文件
    for txt_file in txt_files:
        # 获取文件名（不包括扩展名）
        base_name = os.path.splitext(txt_file)[0]
        
        # 定义输出文件名
        output_file = f"{base_name}.pep.fasta"
        
        # 构建seqtk命令
        command = f"seqtk subseq {genome_file} {os.path.join(input_folder, txt_file)} > {output_file}"
        
        # 执行命令
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process txt files and run seqtk subseq.')
    parser.add_argument('input_folder', type=str, help='Path to the input folder containing txt files')
    parser.add_argument('genome_file', type=str, help='Path to the genome file')
    args = parser.parse_args()
    
    process_files(args.input_folder, args.genome_file)
