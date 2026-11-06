#你的任务： 请编写一个名为 load_prompts() 的函数。

#代码要求：

#使用 try...except 结构。
#在 try 块中：
#使用 with open 以只读模式 ('r') 和 utf-8 编码打开 prompts.json。
#使用 json.load() 读取数据，并将其 return 返回。
#在 except 块中处理两种“翻车”情况（Plan B）：
#捕获 FileNotFoundError（文件不存在）：打印一句提示（比如“未找到Prompt库，将创建新的”），然后 return []（返回空列表）。
#捕获 json.JSONDecodeError（JSON格式损坏）：打印一句警告（比如“Prompt库格式损坏，已重置”），然后 return []。

import json

# 在路径前面加个 r，表示这是原始字符串，防止转义字符出问题
file_path = r'C:\Users\Rebecca\Desktop\AI应用study\课前python练习\prompts.json'
def load_prompts():
    try:
        with open('file_path', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("未找到Prompt库，将创建新的")
        return []
    except json.JSONDecodeError:
        print("Prompt库格式损坏，已重置")
        return []

print(load_prompts())


#请编写 save_prompts(prompts_data) 函数。

def save_prompts(prompts_data):
	try:
		with open(file_path, 'w', encoding='utf-8') as file:
			json.dump(prompts_data, file, ensure_ascii=False, indent=4)
	except Exception as e:
		print(f"保存Prompt库时出错: {e}")

#print(save_prompts([{"prompt": "Hello, world!"}]))

