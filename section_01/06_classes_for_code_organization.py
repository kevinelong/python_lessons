###
# Class - a class is defines a recipe for how to build an Object instance
#           like a recipe for cake defines the steps to make a cake,
#           but executing those steps constructs a new cake instance.
###


# define a new class Person based on the existing class "object"
class Person(object):

    # Constructor
    def __init__(self, first_name, last_name):
        # define two properties and copy initial arguments into them
        self.first_name = first_name
        self.last_name = last_name

    # Method to get string containing both first and last name
    def get_full_name(self):
        return self.first_name + " " + self.last_name


# define a new class Group based on the existing class "list"
# that inherits all of the list class's properties and methods

class Group(list):
    # Group has no constructor it inherited from list

    # Method
    def show(self):
        # loop through all items in list
        for person in self:
            # print the string returned by each items
            print(person.get_full_name())


# define a variable g and put an instance of a new Group into it.
g = Group()

# define a variable p and put an instance of a new Person into it.
# passing in

# create a person named Kevin
p = Person("Kevin", "Long")

# Print only his first name
print (p.first_name)

# put kevin into the group
g.append(p)

# put three more people into the group
g.append(Person("Zoe", "Zither"))
g.append(Person("Billy", "Barrister"))
g.append(Person("Henry", "Harvester"))

# pul out only first person from the group
k = g[0]
# Print that persons last name.
print(k.last_name)

# Print the full name of everyone in the Group/list
g.show()
