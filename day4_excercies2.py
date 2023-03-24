class Number:

     def __init__(self, datatype, value):
         self.datatype=datatype
         self.value=value

    def get_datatype(self):
        return self.datatype

    def set_datatype(self,datatype):
            self.datatype=datatype

    def get_value(self):
        return self.value

    def set_value(self, value):
        if type(self.value) == type(value):
            self.value=value
        else:
            self.datatype= str(type(value))
            self.value=value

