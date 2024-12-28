import os
from dotenv import load_dotenv
from ssl import create_default_context, CERT_NONE
from elasticsearch import Elasticsearch

# .envファイルの読み込み
load_dotenv()

# 環境変数から設定を取得
elastic_url = os.getenv("ELASTIC_URL")
elastic_user = os.getenv("ELASTIC_USER")
elastic_password = os.getenv("ELASTIC_PASSWORD")
ca_certs_path = os.getenv("CA_CERTS_PATH")

# Elasticsearchクライアント作成
ssl_context = create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = CERT_NONE

es = Elasticsearch(
    hosts=[elastic_url],
    basic_auth=(elastic_user, elastic_password),
    ca_certs=ca_certs_path
)

# 接続確認
if es.ping():
    print("Elasticsearchに接続成功")
else:
    print("Elasticsearchに接続できません")

# プレイヤーデータのリスト
players = [
    {"name": "John Doe", "team": "Lions", "position": "Pitcher", "number": 12, "batting_average": 0.275, "home_runs": 20, "runs": 65, "stolen_bases": 5},
    {"name": "Jane Smith", "team": "Tigers", "position": "Catcher", "number": 7, "batting_average": 0.310, "home_runs": 10, "runs": 45, "stolen_bases": 2},
    {"name": "Mike Johnson", "team": "Bears", "position": "First Base", "number": 22, "batting_average": 0.290, "home_runs": 15, "runs": 50, "stolen_bases": 3},
    {"name": "Emily Davis", "team": "Hawks", "position": "Second Base", "number": 5, "batting_average": 0.305, "home_runs": 8, "runs": 40, "stolen_bases": 7},
    {"name": "Chris Brown", "team": "Eagles", "position": "Third Base", "number": 10, "batting_average": 0.285, "home_runs": 12, "runs": 55, "stolen_bases": 4},
    {"name": "Sarah Wilson", "team": "Panthers", "position": "Shortstop", "number": 3, "batting_average": 0.320, "home_runs": 18, "runs": 60, "stolen_bases": 6},
    {"name": "David Clark", "team": "Wolves", "position": "Left Field", "number": 25, "batting_average": 0.275, "home_runs": 22, "runs": 70, "stolen_bases": 5},
    {"name": "Laura Martinez", "team": "Dragons", "position": "Center Field", "number": 11, "batting_average": 0.310, "home_runs": 10, "runs": 45, "stolen_bases": 2},
    {"name": "Peter Lee", "team": "Sharks", "position": "Right Field", "number": 8, "batting_average": 0.290, "home_runs": 14, "runs": 55, "stolen_bases": 3},
    {"name": "Alice Turner", "team": "Cobras", "position": "Catcher", "number": 6, "batting_average": 0.295, "home_runs": 9, "runs": 40, "stolen_bases": 7},
    {"name": "James Harris", "team": "Stallions", "position": "Pitcher", "number": 17, "batting_average": 0.270, "home_runs": 5, "runs": 30, "stolen_bases": 2},
    {"name": "Jessica White", "team": "Titans", "position": "First Base", "number": 13, "batting_average": 0.300, "home_runs": 15, "runs": 50, "stolen_bases": 5},
    {"name": "Kevin Moore", "team": "Owls", "position": "Second Base", "number": 18, "batting_average": 0.280, "home_runs": 12, "runs": 45, "stolen_bases": 4},
    {"name": "Linda Taylor", "team": "Bulls", "position": "Third Base", "number": 4, "batting_average": 0.315, "home_runs": 20, "runs": 65, "stolen_bases": 8},
    {"name": "Brian Anderson", "team": "Hawks", "position": "Shortstop", "number": 14, "batting_average": 0.275, "home_runs": 10, "runs": 40, "stolen_bases": 5},
    {"name": "Megan Thomas", "team": "Panthers", "position": "Left Field", "number": 7, "batting_average": 0.305, "home_runs": 8, "runs": 35, "stolen_bases": 3},
    {"name": "Steven Jackson", "team": "Dragons", "position": "Center Field", "number": 19, "batting_average": 0.290, "home_runs": 13, "runs": 50, "stolen_bases": 6},
    {"name": "Karen Roberts", "team": "Wolves", "position": "Right Field", "number": 16, "batting_average": 0.310, "home_runs": 18, "runs": 60, "stolen_bases": 7},
    {"name": "Richard Lewis", "team": "Lions", "position": "Catcher", "number": 20, "batting_average": 0.300, "home_runs": 22, "runs": 65, "stolen_bases": 4},
    {"name": "Angela Walker", "team": "Sharks", "position": "Pitcher", "number": 5, "batting_average": 0.280, "home_runs": 7, "runs": 35, "stolen_bases": 2},
    {"name": "Matthew Young", "team": "Tigers", "position": "First Base", "number": 24, "batting_average": 0.295, "home_runs": 14, "runs": 50, "stolen_bases": 5},
    {"name": "Elizabeth Hall", "team": "Cobras", "position": "Second Base", "number": 21, "batting_average": 0.310, "home_runs": 8, "runs": 45, "stolen_bases": 3},
    {"name": "Thomas Hernandez", "team": "Owls", "position": "Third Base", "number": 9, "batting_average": 0.275, "home_runs": 13, "runs": 55, "stolen_bases": 6},
    {"name": "Donna King", "team": "Eagles", "position": "Shortstop", "number": 15, "batting_average": 0.300, "home_runs": 12, "runs": 50, "stolen_bases": 4},
    {"name": "Paul Scott", "team": "Bulls", "position": "Left Field", "number": 13, "batting_average": 0.290, "home_runs": 17, "runs": 60, "stolen_bases": 5},
    {"name": "Nancy Green", "team": "Titans", "position": "Center Field", "number": 6, "batting_average": 0.305, "home_runs": 11, "runs": 45, "stolen_bases": 3},
    {"name": "George Adams", "team": "Stallions", "position": "Right Field", "number": 2, "batting_average": 0.320, "home_runs": 10, "runs": 50, "stolen_bases": 4},
    {"name": "Betty Nelson", "team": "Lions", "position": "Catcher", "number": 18, "batting_average": 0.275, "home_runs": 15, "runs": 55, "stolen_bases": 6},
    {"name": "Joshua Baker", "team": "Hawks", "position": "Pitcher", "number": 11, "batting_average": 0.300, "home_runs": 9, "runs": 40, "stolen_bases": 3},
    {"name": "Barbara Hill", "team": "Panthers", "position": "First Base", "number": 23, "batting_average": 0.310, "home_runs": 19, "runs": 65, "stolen_bases": 8}
]

# データをElasticsearchに投入
for i, player in enumerate(players):
    es.index(index="baseball_players", id=i+1, document=player)

print("データのインデックスが完了しました。")