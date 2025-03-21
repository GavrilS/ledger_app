"""
A class to create/delete new Users.
"""

class User:

    def __init__(self, id=None, name=None, password=None, email=None):
        self._id = id
        self.name = name
        self.password = password
        self.email = email

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise Exception('Cannot create a new user without name...')
        
        self._name = name
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        if not password:
            raise Exception('Password is required...')
        
        self._password = password
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if not email:
            raise Exception('Email cannot be empty...')
        
        self._email = email

    def __str__(self):
        return f"User: name -> {self.name}; email -> {self.email}"