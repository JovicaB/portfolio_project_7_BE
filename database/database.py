from abc import ABC, abstractmethod
import MySQLdb


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass


class Database(ABC):
    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def read_data(self, sql_query):
        raise NotImplementedError("Subclasses must implement the 'read_data' method.")

    @abstractmethod
    def save_data(self, sql_query, data):
        raise NotImplementedError("Subclasses must implement the 'save_data' method.")


class MySQLConnection(DatabaseConnection):
    """
    This class extends the functionality of the DatabaseConnection class and provides a method to connect to a specific database. It uses the MySQLdb library to establish the connection.
    """
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            password = 'o5!6i84P.j6>y',
            database="etp",
            port=3306,
            charset='utf8mb4'
        )

        return connection

    def close(self):
        if self.connection:
            self.connection.close()


class DatabaseManager(Database):
    """
    A class that manages reading and saving data to database
    """
    def __init__(self, connection):
        self.connection = connection

    def read_data(self, sql_query, params=None):
        '''
        example usage: member_id = self.database_manager.read_data_sql_query("SELECT user_id from user WHERE JMBG = %s", (jmbg,))
        '''
        connection = self.connection.connect()
        cursor = connection.cursor()
        cursor.execute(sql_query, params)
        data = cursor.fetchall()
        connection.close()
        return data

    def save_data(self, sql_query, data=None):
        try:
            connection = self.connection.connect()
            cursor = connection.cursor()
            cursor.execute(sql_query, data)
            connection.commit()
            connection.close()
        except Exception as e:
            print(f"An error occurred while saving the data to the database: {e}")
            return None

        return None

