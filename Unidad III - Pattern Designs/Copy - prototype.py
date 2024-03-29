import copy
 
class Car:
        '''Prototypical class'''
        def __init__(self):
                ''''Gives each object three attributes and initializes them to default values'''
                self.engine = "3200cc"
                self.color = "Blue"
                self.seats = "5"
        def __str__(self):
                '''Returns the string representation of the object when we print the object.'''
                return  '{} | {} | {}'. format(self.engine, self.color, self.seats)
 
class Prototype:
        '''Prototype class'''
        def __init__(self):
                '''Creates a dictionary object which stores to-be-cloned objects'''
                self._toBeClonedObjects = {}
        def registerObject(self, name, obj):
                '''Registers the object to be cloned. It takes two arguments, 'name' & 'obj'. These values denote the key-value pair
                 which will be entered in the dictionary that contains the to-be-cloned objects.'''
                self._toBeClonedObjects[name] = obj
        def unregisterObject(self, name):
                '''Deletes the mentioned to-be-cloned object from the dictionary.'''
                del self._toBeClonedObjects[name]
        def clone(self, name, **kwargs):
                '''Clones/Replicates the prototypical object. Deepcopy is used for cloning, since it creates new compound object with fresh copies of attributes found in the original. The clone method provides a way of updating the basic attributes of the basic object. The __dict__ represents all the attributes of the object i.e. engine, color & seats. Returns the cloned object.'''
                clonedObject = copy.deepcopy(self._toBeClonedObjects.get(name))
                clonedObject.__dict__.update(kwargs)
                return clonedObject
 
defaultCar = Car()                                                      # Prototypical object: this is the object that will be cloned.
prototype = Prototype()
prototype.registerObject('basicCar', defaultCar)            # registering the defaultCar in toBeCloned dictionary with its key as 'basicCar'
 
carOne = prototype.clone('basicCar')                          # Cloned object
print("Details of carOne:", carOne)                             # OUTPUT: Details of carOne: 3200cc | Blue | 5
 
carTwo = prototype.clone('basicCar', color = "Black")  # another Cloned object
print("Details of carTwo:", carTwo)                             # OUTPUT: Details of carTwo: 3200cc | Black | 5
