#Author:David Oti-George
#Date:January 3, 2024
#Python Class for all Request related queries
#Each method will post a different set of data

from connections import mysql

class postRequestDatas(object):
    def __init__(self):
        self.cursor = mysql.connection.cursor()

    def addNewRequest(self, request_id, request_admin, request_user, pickup_date, request_date):
        try:
            self.cursor = mysql.connection.cursor()
            # Use parameterized queries to avoid SQL injection
            self.cursor.execute(
                "INSERT INTO Request (request_id, request_admin, request_user, pickup_date, request_date) "
                "VALUES (%s, %s, %s, %s, %s)",
                (request_id, request_admin, request_user, pickup_date, request_date)
            )
            mysql.connection.commit()
            self.cursor.close()
            return "Done!!"
        except Exception as e:
            print('Error in addNewRequest:', str(e))
            return "Failed to add request"
        
    def deleteRequest(self, request_id):
        try:
           
            self.cursor = mysql.connection.cursor()
            # Use parameterized queries to avoid SQL injection
            self.cursor.execute(
                "Delete FROM Request WHERE request_id = %s", (request_id)
            )
            mysql.connection.commit()
            self.cursor.close()
            return "Done!!"
        except Exception as e:
            print('Error in deleteRequest:', str(e))
            return "Failed to delete request"
        

    def updateRequest(self, request_id, admin_email, currrent_date):
        try:
            self.cursor = mysql.connection.cursor()
            # Use parameterized queries to avoid SQL injection
            self.cursor.execute(
                "UPDATE Request SET request_admin = %s, pickup_date = %s  WHERE request_id = %s", (admin_email, currrent_date, request_id)
            )
            mysql.connection.commit()
            self.cursor.close()
            return "Done!!"
        except Exception as e:
            print('Error in updateRequest:', str(e))
            return "Failed to update Request "
