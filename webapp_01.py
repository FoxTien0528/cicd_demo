from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# 示例用户名和密码，实际使用时请替换为安全的凭证
users = {
    "username": "password",
    "testuser001": "password",
    "testuser002": "password"
}

@auth.verify_password
def verify_password(username, password):
    # 检查用户名和密码是否匹配
    if username in users and users[username] == password:
        return username

# 使用身份验证装饰器保护API路由
@app.route('/api/myfunction', methods=['GET'])
@auth.login_required
def my_function():
    # 构建一个JSON对象
    response_object = {
        "message": "Hello, this is a JObject response from Azure Function!",
        "status": "success"
    }

    # 返回JSON响应
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True)

 