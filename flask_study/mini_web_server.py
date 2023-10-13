# 1. 导入 Flask 模块
# 2. 创建Flask应用程序实例
from flask import Flask

app = Flask(__name__)

# 通过装饰器@app.route添加路由
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# 通过装饰器@app.route添加路由
@app.route("/listcases")
def hello_listcases():
    return "<p>返回接口数据</p>"

# 4. 启动程序
if __name__ == '__main__':
    app.run()