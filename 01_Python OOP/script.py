#Create class
class Dog:
    #Constructor
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("whoof!")


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address =  address
        self.contact_number = contact_number


#Instantiate an object of the class
owner1 = Owner("Danny","122 Sptingfield Drive", "888-999")
owner2 = Owner("Sally","123 Sptingfield Drive", "889-999")
dog1 = Dog("Bruce", "Scottish Terrier", owner1)
dog2 = Dog("Freya", "Greyhound", owner2)

#Access method of the class
dog1.bark()
dog2.bark()

#Access Object Properties/ Data Field
print(dog1.name)
print(dog2.breed)

print(dog1.owner.name)
print(dog2.owner.contact_number)