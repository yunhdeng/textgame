# TxtGame

一款基于大模型 API 的文字游戏。

## 安装

### 后端

1. 进入 `backend/` 文件夹
2. 创建并激活虚拟环境
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3. 安装依赖
    ```bash
    pip install -r requirements.txt
    ```
4. 设置 `.env` 文件，添加你的 OpenAI API 密钥
5. 运行后端服务器
    ```bash
    python app.py
    ```

### 前端

1. 进入 `frontend/` 文件夹
2. 安装依赖
    ```bash
    npm install
    ```
3. 运行前端应用
    ```bash
    npm run serve
    ```

## 使用

打开浏览器访问 `http://localhost:8080`，即可开始游戏。 