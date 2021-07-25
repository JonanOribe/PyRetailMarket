from typing import List

class Author(User):
    def __init__(self,reviews: List[int]):
        super().__init__()
        self.reviews = reviews