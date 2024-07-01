import os
import subprocess
import argparse

def run_blastp_on_all_files(input_dir, output_dir, db, evalue='1e-5'):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.fa'):
            # 构造文件路径
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename.replace('.fa', '.blastout'))
            
            # 构建blastp命令
            command = [
                'blastp',
                '-query', input_file,
                '-db', db,
                '-evalue', evalue,
                '-outfmt', '6 std qlen slen',
                '-out', output_file
            ]
            
            # 执行blastp命令
            subprocess.run(command)
            print(f'Processed {input_file} and saved output to {output_file}')

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Run blastp on all fasta files in a directory.")
    parser.add_argument('input_directory', type=str, help="Directory containing input fasta files")
    parser.add_argument('output_directory', type=str, help="Directory to save the blastp output files")
    parser.add_argument('db', type=str, help="Database to use for blastp")
    args = parser.parse_args()
    
    # 运行blastp
    run_blastp_on_all_files(args.input_directory, args.output_directory, args.db)
