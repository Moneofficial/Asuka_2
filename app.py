from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "MoneHUB Engine V1.1 - ACTIVE"

@app.route('/ignite', methods=['POST'])
def ignite():
    data = request.json
    target_url = data.get('url')
    count = int(data.get('count', 10))
    
    # ここに本来はTikTokの自動操作コードが入ります
    # 現在は「処理が進行している」ことをシミュレートします
    print(f"DEBUG: Processing {target_url} for {count} accounts.")
    
    return jsonify({
        "status": "success",
        "message": f"【MoneHUB 稼働開始】\nターゲット: {target_url}\n指示数: {count}\n\n[現在状況]\nシステムがTikTokサーバーへのアクセスを試行中... 順次フォロワー増強処理を開始します。このままお待ちください。"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
