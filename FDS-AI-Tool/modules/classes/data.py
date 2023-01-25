class Dataset:
    """
    A class that creates an object that can store and manage a dictionary of data.

    Attributes:
        data (dict): A dictionary that stores the data.

    Methods:
        __init__(): Initializes an empty dictionary called `self.data`.
        add(name, data): Adds the `data` to the `self.data` dictionary with the key `name`.
        remove(name): Deletes the key-value pair from the `self.data` dictionary.
        get_data(name): Returns the value associated with `name` key in the `self.data` dictionary.
        list_name(): Returns a list of all the keys in the `self.data` dictionary. If the dictionary is empty, it returns an empty list.
        get_shape(): Returns two lists with the number of rows and number of columns for each value in the `self.data` dictionary. If the dictionary is empty, it returns two empty lists.
    """

    def __init__(self):
        """
        Initializes an empty dictionary called `self.data`.
        """
        self.data = {}

    def add(self, name, data):
        """
        Adds the `data` to the `self.data` dictionary with the key `name`.

        Args:
            name (str): the key for the data
            data: the value to be added to the dictionary

        """
        self.data[name] = data

    def remove(self, name):
        """
        Deletes the key-value pair from the `self.data` dictionary.

        Args:
            name (str): the key of the data to be removed

        """
        del self.data[name]

    def get_data(self, name):
        """
        Returns the value associated with `name` key in the `self.data` dictionary.

        Args:
            name (str): the key of the data to be retrieved

        Returns:
            data: the value associated with the key 'name'

        """
        return self.data[name]

    def list_name(self):
        """
        Returns a list of all the keys in the `self.data` dictionary.
        If the dictionary is empty, it returns an empty list.

        Returns:
            list: list of keys in the dictionary

        """
        if bool(self.data):  # if data isn't empty
            return list(self.data.keys())
        else:
            return []

    def get_shape(self):
        """
        Returns two lists with the number of rows and number of columns for each value in the `self.data` dictionary.
        If the dictionary is empty, it returns two empty lists.

        Returns:
            tuple: two lists with the number of rows and number of columns for each value in the `self.data` dictionary
        """
        if bool(self.data):
            data_shape = [data.shape for data in self.data.values()]
            n_rows = [shape[0] for shape in data_shape]
            n_cols = [shape[1] for shape in data_shape]
            return n_rows, n_cols
        else:
            return [], []
