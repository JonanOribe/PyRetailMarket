from src.models.user import User

class Buyer(User):
    def __init__(self, name: str, phone: str, email: str, birthday: str,user_type: str, shopping_cart: int):
        User.__init__(self, name, phone, email, birthday,user_type)
        self.shopping_cart = shopping_cart
        
    @property
    def shopping_cart(self):
        return self.shopping_cart
    
    @shopping_cart.setter
    def shopping_cart(self, new_shopping_cart: str):
        if type(new_shopping_cart) == str:
            self._shopping_cart = new_shopping_cart
        else:
            raise Exception("Invalid value for shopping_cart")
    
    def __str__(self):
        return 'Name: {}, phone: {}, email: {}, birthday: {}, user_type: {}, shopping_cart: {}'.format(self._name,self._phone,self._email,self._birthday,self._user_type, self._shopping_cart)