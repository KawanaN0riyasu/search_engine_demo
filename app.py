from flask import Flask, request, render_template, jsonify
from elasticsearch import Elasticsearch
from ssl import create_default_context, CERT_NONE
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# Elasticsearch設定
elastic_url = os.getenv("ELASTIC_URL")
elastic_user = os.getenv("ELASTIC_USER")
elastic_password = os.getenv("ELASTIC_PASSWORD")
ca_certs_path = os.getenv("CA_CERTS_PATH")

ssl_context = create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = CERT_NONE

es = Elasticsearch(
    elastic_url,
    basic_auth=(elastic_user, elastic_password),
    ca_certs=ca_certs_path
)

app = Flask(__name__)

@app.route('/')
def home():
    """検索画面を表示"""
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    """
    Elasticsearchを利用した選手データ検索
    """
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({"error": "クエリが空です"}), 400

    try:
        # Elasticsearch検索クエリ
        search_body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["name", "team", "position"],
                    "fuzziness": "AUTO"
                }
            }
        }
        response = es.search(index="baseball_players", body=search_body)
        hits = response['hits']['hits']

        # 検索結果を整形して返す
        results = [
            {
                "id": hit["_id"],
                "score": hit["_score"],
                "source": hit["_source"]
            }
            for hit in hits
        ]
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")