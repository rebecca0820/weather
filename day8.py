#调用API

import json

import requests



# 1. 准备请求地址和参数
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 30.25,      # 纬度（杭州）
    "longitude": 120.16,    # 经度（杭州）
    "current": "temperature_2m,weather_code"
}

# 2. 发送请求
resp = requests.get(url, params=params, timeout=5)


# 3. 检查接口是否正常返回
resp.raise_for_status()

# 4. 把 JSON 转成 Python 字典
data = resp.json()
print(data)

# 5. 打印原始结构（先看清长什么样）
#import json
#print(json.dumps(data, indent=4, ensure_ascii=False))


temp = data["current"]["temperature_2m"]
code = data["current"]["weather_code"]
print(f"当前温度：{temp}℃，天气代码：{code}")
# 如果哪天接口改版，current 字段没了，或者网络返回了错误结构，程序会直接崩，所以正式写法要加保护：
current = data.get("current", {})
temp = current.get("temperature_2m", "未知")
