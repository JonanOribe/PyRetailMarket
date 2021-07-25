from typing import List
from src.models.user import User

class Author(User):
    def __init__(self, name: str, phone: str, email: str, birthday: str,user_type: str, reviews: List[int]):
        User.__init__(self, name, phone, email, birthday,user_type)
        self.reviews = reviews
        
    @property
    def reviews(self):
        return self._reviews
    
    @email.setter
    def email(self, new_reviews):
        if type(new_reviews) == str:
            self._reviews = new_reviews
        else:
            raise Exception("Invalid value for email")
        
        def __str__(self):
            return 'Name: {}, phone: {}, email: {}, birthday: {}, user_type: {}, reviews: {}'.format(self._name,self._phone,self._email,self._birthday,self._user_type,self.reviews)