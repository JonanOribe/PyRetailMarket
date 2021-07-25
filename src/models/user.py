class User():
    
    def __init__(self, name: str, phone: str, email: str, birthday: str,user_type: str):
        self._name = name 
        self._phone = phone 
        self._email = email 
        self._birthday = birthday
        self._user_type = user_type
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if type(new_name) == str:
            self._name = new_name
        else:
            raise Exception("Invalid value for name")
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, new_phone: str):
        if type(new_phone) == str and len(new_phone)>8:
            self._phone = new_phone
        else:
            raise Exception("Invalid value for phone")
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if (type(new_email) == str) and ('@' in new_email):
            self._email = new_email
        else:
            raise Exception("Invalid value for email")
        
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, new_birthday):
        if (type(new_birthday) == str) and ('/' in new_birthday):
            self._birthday = new_birthday
        else:
            raise Exception("Invalid value for birthday")
        
    @property
    def user_type(self):
        return self._user_type
    
    @user_type.setter
    def user_type(self, new_user_type):
        if (type(new_user_type) == str):
            self._user_type = new_user_type
        else:
            raise Exception("Invalid value for user_type")
        
    def __str__(self):
        return 'Name: {}, phone: {}, email: {}, birthday: {}, user_type: {}'.format(self._name,self._phone,self._email,self._birthday,self._user_type)
        
        