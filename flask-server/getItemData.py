#Author:David Oti-George
#Date:January 3, 2024
#Python Class for all item related queries
#Each method will retrieve a different set of data

from connections import mysql

class getItemDatas(object):
    def __init__(self):
        self.cursor = mysql.connection.cursor()

    def getAlldata(self):
        self.cursor = mysql.connection.cursor()
        self.cursor.execute("SELECT * FROM Item")
        iData = self.cursor.fetchall()
        self.cursor.close()
        return iData
    
    def getItemQuantities(self):
        self.cursor = mysql.connection.cursor()
        self.cursor.execute("SELECT item_name, quantity FROM Item")
        iData = self.cursor.fetchall()
        self.cursor.close()
        return iData
    
    def getAnItemName(self, item_name):
        self.cursor = mysql.connection.cursor()
        self.cursor.execute(f"""SELECT item_name FROM Item WHERE item_name = '{item_name}'""")
        iData = self.cursor.fetchall()
        self.cursor.close()
        return iData