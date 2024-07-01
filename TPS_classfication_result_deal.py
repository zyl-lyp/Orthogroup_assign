import os
import csv
import argparse
import openpyxl

def process_csv_and_count(input_directory):
    # 创建新的Excel工作簿
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Counts"
    ws.append(["Folder Name", "Count"])

    # 遍历TPS_out文件夹下的每个子文件夹
    for folder in os.listdir(input_directory):
        csv_file_path = os.path.join(input_directory, folder, "monoTP_dir", "high_confidence_final_results.csv")
        if os.path.exists(csv_file_path):
            try:
                with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)  # 跳过第一行（标题行）
                    count = sum(1 for row in reader if row[0].strip())  # 计算第一列非空值的数量
            except Exception as e:
                print(f"Error reading file {csv_file_path}: {str(e)}")
                continue

            # 添加计数到Excel文件
            ws.append([folder, count])
            print(f'Processed {csv_file_path}')
        else:
            print(f"No CSV file found in: {csv_file_path}")

    # 保存Excel文件
    output_excel_file = os.path.join(input_directory, 'HighConfidenceCounts.xlsx')
    wb.save(output_excel_file)
    print(f'Excel file saved as {output_excel_file}')

if __name__ == '__main__':
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Count non-empty entries in the first column of high_confidence_final_results.csv from each subdirectory and write the counts to an Excel file.")
    parser.add_argument('input_directory', type=str, help="The root directory containing subdirectories with CSV files to process.")
    args = parser.parse_args()

    # 运行函数
    process_csv_and_count(args.input_directory)
