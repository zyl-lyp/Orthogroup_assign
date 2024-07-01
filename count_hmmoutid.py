import os
import glob
import argparse
import openpyxl

def count_non_comment_lines(input_directory):
    # 创建新的Excel工作簿
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Counts"
    ws.append(["File Name", "Count"])

    # 搜索目录下所有的 _out.id 结尾的文件
    search_path = os.path.join(input_directory, '*_out.id')
    id_files = glob.glob(search_path)

    if not id_files:
        print(f"No '_out.id' files found in the directory: {input_directory}")
        return

    for file_path in id_files:
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue

        count = 0
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if not line.strip().startswith('#'):
                        count += 1
        except Exception as e:
            print(f"Error reading file {file_path}: {str(e)}")
            continue
        
        # 从文件名提取所需的部分
        base_name = os.path.basename(file_path)
        file_name = base_name.replace('_out.id', '')
        
        # 添加到Excel文件
        ws.append([file_name, count])
    
    # 保存Excel文件
    output_excel_file = 'PRISE_hmmout.xlsx'
    wb.save(output_excel_file)
    print(f'Excel file saved as {output_excel_file}')

if __name__ == '__main__':
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Count non-comment lines in files ending with _out.id and write the counts to an Excel file.")
    parser.add_argument('input_directory', type=str, help="The directory containing _out.id files to process.")
    args = parser.parse_args()

    # 运行函数
    count_non_comment_lines(args.input_directory)

