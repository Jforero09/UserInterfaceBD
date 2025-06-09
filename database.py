import oracledb

def get_connection():

        connection = oracledb.connect(
            user="interfaceUser",
            password="password123",
            dsn="localhost:1521/XEPDB1"
        )
        return connection

        