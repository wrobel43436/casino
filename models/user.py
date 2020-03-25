import json


class User:
    def __init__(self):
        self.email = None
        self.first_name = None
        self.last_name = None
        self.is_admin = None
        self.is_active = None
        self.last_login = None
        self.password = None

    def from_json(self, json):
        self.email = json['email']
        self.first_name = json['firstName']
        self.last_name = json['lastName']
        self.is_admin = json['isAdmin']
        self.is_active = json['isActive']
        self.last_login = json['lastLogin']
        self.password = json['password']


    def to_json(self):
        json_response = {}
        json_response['email'] = self.email
        json_response['firstName'] = self.first_name
        json_response['lastName'] = self.last_name
        json_response['isAdmin'] = self.is_admin
        json_response['isActive'] = self.is_active
        json_response['lastLogin'] = self.last_login
        json_response['password'] = self.password


        return json_response