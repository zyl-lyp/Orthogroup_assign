import os
import glob
import subprocess
import argparse

def run_search_tps(input_directory, output_directory, script_path):
    # 定义固定的路径
    class_specific_hmms = '/home/penglan/workspace/IGs_analysis/Asteraceae/TPS-main/class-specific_hmms'
    score_table = '/home/penglan/workspace/IGs_analysis/Asteraceae/TPS-main/score_table'
    pfams_dir = '/home/penglan/workspace/IGs_analysis/Asteraceae/TPS-main/pfams_dir'
    
    # 查找所有.fa结尾的文件
    search_path = os.path.join(input_directory, '*.fa')
    fasta_files = glob.glob(search_path)
    
    for fasta_file in fasta_files:
        # 为每个文件创建一个以文件名命名的结果目录
        base_name = os.path.basename(fasta_file).replace('.fa', '')
        file_output_dir = os.path.join(output_directory, base_name)
        os.makedirs(file_output_dir, exist_ok=True)
        
        # 构建命令
        command = [
            'perl', script_path,
            '-d', class_specific_hmms,
            '-i', fasta_file,
            '-t', score_table,
            '-s', '1',
            '-p', pfams_dir,
            '-o', file_output_dir
        ]
        
        # 执行命令
        subprocess.run(command)
        print(f'Processed {fasta_file} and output to {file_output_dir}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run search_TPS.pl on .fa files in a directory with specified output directory.")
    parser.add_argument('input_directory', type=str, help="Directory containing .fa files.")
    parser.add_argument('output_directory', type=str, help="Root directory to save the output files.")
    args = parser.parse_args()

    # 确保输出目录存在
    os.makedirs(args.output_directory, exist_ok=True)

    # 指定 search_TPS.pl 脚本的路径
    script_path = '/home/penglan/workspace/IGs_analysis/Asteraceae/TPS-main/search_TPS.pl'
    
    # 执行搜索函数
    run_search_tps(args.input_directory, args.output_directory, script_path)

