import sqlite3
def read_dumpsters():
    try:
        sqlite_connection = sqlite3.connect('test.db')
        cursor = sqlite_connection.cursor()
        print('comlete')

        sqliete_select_query = """SELECT * FROM dumpsters"""
        cursor.execute(sqliete_select_query)
        records = cursor.fetchall()
        ans = []
        print(type(records))
        for i in records:
            ans.append(i)
            ans.append('qq')
        cursor.close()
        print(ans)
        return ans
    except sqlite3.Error as error:
        print(error)

