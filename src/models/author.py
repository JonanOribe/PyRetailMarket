class Author(User):
    def __init__(self,reviews: []):
        super().__init__()
        self.reviews = reviews