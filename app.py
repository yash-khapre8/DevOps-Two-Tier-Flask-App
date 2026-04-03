from flask import Flask
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="172.31.46.3",
    user="appuser",
    password="StrongPass123",
    database="devopsdb"
)

@app.route('/')
def home():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    return str(cursor.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
