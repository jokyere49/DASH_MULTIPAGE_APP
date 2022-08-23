import pandas as pd
import sqlite3

def test_db(conn):
    c = conn.cursor()
    df = pd.read_sql('select * from users', conn)
    print(df)

if __name__ == '__main__':
    conn = sqlite3.connect('data.sqlite')
    test_db(conn)