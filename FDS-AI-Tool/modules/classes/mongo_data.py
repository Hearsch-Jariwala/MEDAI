from pymongo import MongoClient


class Dataset:
    """
    A class for storing and manipulating data using MongoDB
    """

    def __init__(self):
        """
        Initialize a MongoClient object to connect to a MongoDB server
        Initialize a MongoDB database object and a collection object
        """
        self.client = MongoClient()
        self.db = self.client.your_db_name
        self.collection = self.db.your_collection_name

    def add(self, name, data):
        """
        Add data to the collection with the corresponding name
        :param name: name of the data (string)
        :param data: data to be stored (ndarray)
        :return: None
        """
        self.collection.insert_one({"name": name, "data": data})

    def remove(self, name):
        """
        Remove data from the collection that corresponds to the given name
        :param name: name of the data (string)
        :return: None
        """
        self.collection.delete_one({"name": name})

    def get_data(self, name):
        """
        Get the data from the collection that corresponds to the given name
        :param name: name of the data (string)
        :return: data (dictionary)
        """
        return self.collection.find_one({"name": name})

    def list_name(self):
        """
        Get a list of names of data in the collection
        :return: list of names (list of strings)
        """
        return [x["name"] for x in self.collection.find()]

    def get_shape(self):
        """
        Get the shape of data in the collection
        :return: tuple of two lists, first list contains the number of rows and second list contains the number of columns
        """
        data_shape = [x["data"].shape for x in self.collection.find()]
        n_rows = [shape[0] for shape in data_shape]
        n_cols = [shape[1] for shape in data_shape]

        return n_rows, n_cols
