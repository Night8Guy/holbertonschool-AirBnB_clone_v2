#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def test_create_with_params(self):
        """Test create with params"""
        # Test creating a State with name="California"
    self.console.onecmd('create State name="California"')
    state_id = self.console.stdout.getvalue().strip()
    self.assertTrue(state_id)

    # Test creating a State with name="Arizona"
    self.console.onecmd('create State name="Arizona"')
    state_id = self.console.stdout.getvalue().strip()
    self.assertTrue(state_id)

    # Test creating a Place with multiple parameters
    self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
    place_id = self.console.stdout.getvalue().strip()
    self.assertTrue(place_id)

    # Test showing all State objects
    self.console.onecmd('all State')
    output = self.console.stdout.getvalue().strip()
    self.assertIn('California', output)
    self.assertIn('Arizona', output)

    # Test showing all Place objects
    self.console.onecmd('all Place')
    output = self.console.stdout.getvalue().strip()
    self.assertIn('My little house', output)pass