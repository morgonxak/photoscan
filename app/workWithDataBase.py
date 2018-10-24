import sqlite3

class DBManager:
    def __init__(self, pachDB, SettingsPC):
        self.SettingsPC = SettingsPC
        self.conn = sqlite3.connect(pachDB, check_same_thread=False)  # или :memory: чтобы сохранить в RAM
        self.cursor = self.conn.cursor()

    def pullData(self, DBtable, data):
        '''
        Вставка данных в таблицу принимаетт имя таблицы и [('Exodus', 'Andy Hunter')]
        :param DBtable:
        :param data:
        :return:
        '''

        query = 'INSERT INTO ' + DBtable + ' VALUES (' + '?,'*(len(data[0])-1) + '?)'

        self.cursor.executemany(query, data)
        self.conn.commit()

    def getInfoPeople(self, login, password):
        '''
        Получаем количество денег у пользователя
        :param phone:
        :param password:
        :return:
        '''
        sql = "SELECT NAME, SURNAME, PATRONYMIC FROM people WHERE lOGIN = ? AND PASSWORD = ?"
        wallet = self.cursor.execute(sql, (login, password))
        print()
        return wallet.fetchall()

    def getInfoProcess(self, login):

        wallet = self.cursor.execute("SELECT NAME, CATEGORY, PROCESS FROM treatment WHERE ID = ?", (login,))
        return wallet.fetchall()

    def getSettings(self):
        wallet = self.cursor.execute(
            "SELECT pachImageTemp, pachProject, UserID FROM main.settings WHERE workplace = ?", (self.SettingsPC,))
        return wallet.fetchall()

    def editUserId(self, value):
        wallet = self.cursor.execute("UPDATE settings SET UserID = ? WHERE workplace = ?", (value, self.SettingsPC))
        self.conn.commit()
        return wallet.fetchall()



if __name__ == "__main__":
    test = DBManager(r'C:\projectTree\database.db')
    #a = test.getInfoPeople('testLogin', 'testPassord')
    #c = test.getInfoProcess('morgon')
    b = test.editUserId('PC1', 5)
    print(b)
