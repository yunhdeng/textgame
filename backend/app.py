import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 自定义 API 配置
api_url = "https://api.siliconflow.cn/v1/chat/completions"
api_key = os.getenv("CUSTOM_API_KEY")  # 确保在 .env 中设置了正确的 API 密钥

def generate_content(prompt):
    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        response_data = response.json()
        return response_data['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        print(f"API 请求失败: {e}")
        return "无法生成内容"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "未提供提示"}), 400
    content = generate_content(prompt)
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(debug=True)