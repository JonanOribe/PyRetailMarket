class Accesory():
    def __init__(self, accesory_type: int):
        self._accesory_type = accesory_type
        
    @property
    def accesory_type(self):
        return self.accesory_type
    
    @accesory_type.setter
    def accesory_type(self, new_accesory_type: int):
        if type(new_accesory_type) == str:
            self._accesory_type = new_accesory_type
        else:
            raise Exception("Invalid value for accesory_type")