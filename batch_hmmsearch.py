import os
import subprocess
import argparse

def run_hmmsearch_on_fa_files(input_dir, hmm_file, output_dir):
    # 检查输出目录是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有.fa文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.fa'):
            # 构建输入文件的完整路径
            input_file = os.path.join(input_dir, filename)

            # 去除文件扩展名，用于输出文件命名
            base_name = os.path.splitext(filename)[0]

            # 构建输出文件的路径
            domtblout_path = os.path.join(output_dir, f'{base_name}.domtblout')
            hmmout_path = os.path.join(output_dir, f'{base_name}.hmmout')

            # 构建hmmsearch命令
            command = [
                'hmmsearch',
                '--cut_tc',
                '--domtblout', domtblout_path,
                '-o', hmmout_path,
                hmm_file,
                input_file
            ]
            
            # 执行hmmsearch命令
            subprocess.run(command)
            print(f'Processed {input_file} and saved output to {domtblout_path} and {hmmout_path}')

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Run hmmsearch on all .fa files in a directory.")
    parser.add_argument('input_directory', type=str, help="Directory containing .fa files to process")
    parser.add_argument('hmm_file', type=str, help="Path to the HMM file")
    parser.add_argument('output_directory', type=str, help="Directory to save the hmmsearch output files")
    args = parser.parse_args()
    
    # 运行函数
    run_hmmsearch_on_fa_files(args.input_directory, args.hmm_file, args.output_directory)
