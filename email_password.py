import re

input_file = input("파일 경로를 입력해 주세요.: ")

output_file = 'output.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    data = f.read()

    matches = re.findall(r'([\w\.-]+@[\w\.-]+:\S+)', data)

    with open(output_file, 'w', encoding='utf-8') as f:
        for match in matches:
            f.write(match + '\n')
