import json
import zhconv
import os
from typing import Dict, Any

def convert_to_simplified_chinese(input_file: str) -> None:
    """
    将 JSON 文件中的繁体中文转换为简体中文
    
    Args:
        input_file: 输入的 JSON 文件路径
    """
    # 读取 JSON 文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        data = json.loads(content)
    
    # 遍历并转换数据
    for item in data['data']:
        # 转换 title
        item['title'] = zhconv.convert(item['title'], 'zh-cn')
        
        # 转换 paragraphs 中的内容
        for paragraph in item['paragraphs']:
            # 转换 context
            paragraph['context'] = zhconv.convert(paragraph['context'], 'zh-cn')
            
            # 转换 qas 中的内容
            for qa in paragraph['qas']:
                # 转换 question
                qa['question'] = zhconv.convert(qa['question'], 'zh-cn')
                
                # 转换 answers 中的 text
                for answer in qa['answers']:
                    answer['text'] = zhconv.convert(answer['text'], 'zh-cn')
    
    # 构建输出文件名
    output_file = os.path.splitext(input_file)[0] + '_simplified_chinese.json'
    
    # 保存转换后的 JSON 文件，保持原有格式
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))
    
    print(f'转换完成！输出文件：{output_file}')

if __name__ == '__main__':
    # 定义需要处理的文件列表
    input_files = [
        "./DRCD_dev.json",
        "./DRCD_test.json",
        "./DRCD_train.json"
    ]
    
    # 批量处理文件
    for input_file in input_files:
        print(f'正在处理文件：{input_file}')
        convert_to_simplified_chinese(input_file) 
