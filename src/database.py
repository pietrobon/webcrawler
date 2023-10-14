import os
import datetime
from pymongo import MongoClient
from pymongo.errors import PyMongoError, WriteError, WriteConcernError
from dotenv import load_dotenv

class Database:
    """
    A class to interact with a MongoDB database and perform operations.

    Attributes:
        cotacao (pymongo.collection.Collection): A reference to the 'cotacao' collection in the database.

    Methods:
        - __init__: Initialize the Database instance and establish a connection to the database.
        - connect: Connect to the MongoDB database using the provided URI.
        - insert: Insert a document into the 'cotacao' collection.
        - find_most_recent: Retrieve the most recent document from the 'cotacao' collection.
    """

    def __init__(self):
        """
        Initialize the Database instance and establish a connection to the database.
        """
        load_dotenv()
        self.cotacao = self.connect()

    def connect(self):
        """
        Connect to the MongoDB database using the provided URI.

        Returns:
            pymongo.collection.Collection: A reference to the 'cotacao' collection in the database.

        Raises:
            DatabaseConnectionError: If there is an error while connecting to the database.
        """
        try:
            client = MongoClient(os.getenv('DB_URI'))
            db = client['webcrawler']
            return db.cotacao
        except PyMongoError as e:
            raise DatabaseConnectionError(f"Failed to connect to the database: {e}")

    def insert(self, data: dict):
        """
        Insert a document into the 'cotacao' collection.

        Args:
            data: The document to be inserted.

        Returns:
            str: The ID of the inserted document.

        Raises:
            DatabaseInsertionError: If there is an error while inserting the document.
        """
        try:
            result = self.cotacao.insert_one(data)
            return result.inserted_id
        except (WriteError, WriteConcernError) as e:
            raise DatabaseInsertionError(f"Failed to insert data into the database: {e}")

    def find_most_recent(self, query: dict):
        """
        Retrieve the most recent document from the 'cotacao' collection.

        Args:
            query: A dictionary representing the query criteria to filter documents.

        Returns:
            dict or None: The most recent document that matches the query criteria,
                or None if no matching documents are found.

        Raises:
            DatabaseQueryError: If there is an error while querying the database.
        """
        try:
            result = self.cotacao.find_one(query, sort=[('time_of_extract', -1)])
            return result
        except PyMongoError as e:
            raise DatabaseQueryError(f"Failed to retrieve the most recent data from the database: {e}")

class DatabaseQueryError(Exception):
    pass

class DatabaseInsertionError(Exception):
    pass

class DatabaseConnectionError(Exception):
    pass


if __name__ == "__main__":
    db = Database()
    data = {'currency': 'Dólar Americano', 'cost': '5.14', 'time_of_extract': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    inserted_data = db.insert(data)
    print(inserted_data)
    currency_query = {'currency': 'Dólar Americano'}
    result = db.find_most_recent(currency_query)
    print(result)
