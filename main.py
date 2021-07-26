from src.models.user import User
from src.models.buyer import Buyer
from src.models.author import Author
from src.models.review import Review

if __name__ == "__main__":
    user = User('Peter','778542351','peter@gmail.com','12/07/1992','0')
    print(user)
    user.phone='5543000000'
    print(user)
    
    buyer = Buyer('Luck', '9976547765', 'luck@gmail.com','07/08/2001','1','0')
    buyer.shopping_cart='1'
    print(buyer)
    
    author = Author('John', '9976547765', 'john@gmail.com','14/09/2001','1','1')
    print(author)
    
    review = Review('Opinion', 'Is really good', 1, 2)
    review.content = 'Not so good'
    print(review)