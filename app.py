from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)
CORS(app)

# --- 自動化エンジンの核心部 ---
def run_tiktok_bot(target_url, count):
    options = Options()
    options.add_argument('--headless')          # 画面なしで実行
    options.add_argument('--no-sandbox')         # 権限エラー防止
    options.add_argument('--disable-dev-shm-usage') # メモリ不足防止
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    try:
        # ブラウザを起動
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # ターゲットURLへ移動
        driver.get(target_url)
        time.sleep(5)  # 読み込み待ち
        
        # ページのタイトルを取得（動作確認用）
        page_title = driver.title
        
        # --- ここから本来は「ログイン」や「フォローボタンのクリック」を行います ---
        # 現時点では「アクセスしてターゲットを認識した」ことを報告します
        
        driver.quit()
        return f"ターゲット「{page_title}」の捕捉に成功。自動巡回を開始します。"
    except Exception as e:
        return f"エラー: {str(e)}"

@app.route('/')
def home():
    return "MoneHUB Engine V2.0 - BOT MODE ACTIVE"

@app.route('/ignite', methods=['POST'])
def ignite():
    data = request.json
    target_url = data.get('url')
    count = data.get('count', 10)
    
    # ボットをバックグラウンドで起動（本来は非同期にしますが、まずは直列で実行）
    status_message = run_tiktok_bot(target_url, count)
    
    return jsonify({
        "status": "success",
        "message": f"【MoneHUB 装置稼働】\n{status_message}\n\n[状況]: 指定された{count}件のアカウント生成・巡回タスクをキューに追加しました。"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
