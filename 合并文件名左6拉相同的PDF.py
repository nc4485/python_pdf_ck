# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyMuPDF

import os
import fitz  # PyMuPDF库

# 指定PDF文件夹路径
pdf_folder = r'\\nnn-win7\扫描\7.31CTP\CK'

# 获取文件夹中所有PDF文件
pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]

# 创建一个字典，用于存储相同前6位文件名的PDF文件列表
file_dict = {}

# 根据文件名前6位将PDF文件分组
for file in pdf_files:
    prefix = file[:6]
    if prefix not in file_dict:
        file_dict[prefix] = []
    file_dict[prefix].append(file)

# 合并相同前6位文件名的PDF文件
for prefix, files in file_dict.items():
    output_file = os.path.join(pdf_folder, f"{prefix}.pdf")
    writer = fitz.open()  # 创建一个新的PDF文件
    for file in files:
        pdf_path = os.path.join(pdf_folder, file)
        reader = fitz.open(pdf_path)  # 打开每个PDF文件
        writer.insert_pdf(reader)  # 将当前PDF文件插入新PDF文件中
        reader.close()
    writer.save(output_file)  # 保存新PDF文件
    writer.close()
    print(f"Merged {len(files)} files into {output_file}")

print("PDF files merged successfully!")
