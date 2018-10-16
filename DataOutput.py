
import codecs

class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_file(self):
        pass


    def output_database(self):
        pass


    