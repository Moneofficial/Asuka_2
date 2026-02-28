from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # サイトからの命令を許可する設定

@app.route('/')
def home():
    return "MoneHUB Engine is Running!"

@app.route('/ignite', methods=['POST'])
def ignite():
    data = request.json
    target_url = data.get('url')
    count = data.get('count')
    
    # ここに将来的にTikTok操作コードを追加します
    print(f"Target: {target_url}, Count: {count}")
    
    return jsonify({
        "status": "success",
        "message": f"API接続成功。ターゲット {target_url} への点火準備が完了しました。"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
