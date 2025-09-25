import sqlite3

def init():
    conn = sqlite3.connect("campaigns.db")
    with open("init_db.sql", "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()
    print("✅ Database initialized: campaigns.db")

if __name__ == "__main__":
    init()
