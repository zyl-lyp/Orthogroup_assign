import pandas as pd
import argparse

def process_file(input_file):
    # 读取TSV文件
    df = pd.read_csv(input_file, sep='\t')

    # 获取列名
    headers = df.columns.tolist()

    # 循环处理每一行
    for index, row in df.iterrows():
        row_name = row[0]  # 第一列作为行名
        for col_index, cell in enumerate(row[1:], start=1):
            col_name = headers[col_index]  # 获取列名
            file_name = f"{col_name}.txt"
            
            # 将内容写入对应的txt文件
            with open(file_name, 'a', encoding='utf-8') as txtfile:
                if pd.notna(cell):  # 检查单元格是否为空
                    elements = str(cell).split(',')  # 以逗号分隔元素
                    for element in elements:
                        txtfile.write(element.strip() + '\n')  # 去除多余空格并换行写入

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a TSV file and output to text files.')
    parser.add_argument('input_file', type=str, help='Path to the input TSV file')
    args = parser.parse_args()
    
    process_file(args.input_file)
