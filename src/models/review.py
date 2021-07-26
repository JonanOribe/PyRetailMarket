class Review():
    def __init__(self, title: str, content: str, author: int, product: int):
        self.title = title
        self.content = content
        self.author = author
        self.product = product

    def __str__(self):
        return 'Title: {}, content: {}, author: {}, product: {}'.format(self.title,self.content,str(self.author),str(self.product))