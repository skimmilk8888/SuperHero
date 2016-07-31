import sqlite3

database_file = 'training.db'

def init_db():
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        # create the table
        cursor.execute('create table if not exists training_data (id integer primary key autoincrement, data text, label text)')

def add_record(data, label):
    # insert records
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        cursor.execute('insert into training_data (data, label) values (?, ?)', (unicode(data, 'utf-8'), label))

def read_record(id):
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        cursor.execute("select data, label from training_data where (id = {})".format(id))
        row = cursor.fetchone()
        return (row[0], row[1]) if row else (None, None)

def delete_record(id):
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        cursor.execute("delete from training_data where (id = {})".format(id))
        return cursor.rowcount == 1

def update_record(id, data, label):
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        cursor.execute("update training_data set data = ?, label = ? where id = ?", (data, label, id))

def list_records():
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        cursor.execute("select id from training_data")
        rows = cursor.fetchall()
        ids = []
        for row in rows:
            id, = row
            ids.append(id)
        return ids