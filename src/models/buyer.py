class Buyer(User):
    def __init__(self, shopping_cart: int):
        super().__init__()
        self.shopping_cart = shopping_cart