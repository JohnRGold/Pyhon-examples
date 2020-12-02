"""
An interface is a blueprint that acts similar to a base class, but with the advantages that they are
easier to extend in projects where further functionalities may be added in the future. They also
bypass a series of issues arising from inheritance conflicts in multiple inheritance contexts (see for
instance the diamond problem). It also allows for more dynamic design of classes via the so-called
"duck typing", based on the idea that it is the methods of a class that define its place in the
strcture, not its name and explicit inheritance. In this script you can find an example of informal
interface, used for more informal contexts where class structure expansion is not expected, as well
as a more solid version, implementing a full-fletched interface via meta-classes, which are similar
to abstract classes (classes that are defined internally to a program, unaccessible to by the user
and unable to be instantiated as themselves, but only through their subclasses (called concrete
classes as opposed to abstract classes and interfaces).
"""


class InformalInterfaceSQL:
    def method1(self):
        pass

    def method2(self):
        pass

    ''' Interfaces make explicit the common methods that several classes will have, although
    no implementation is provided, as each class may have its own version of the same named method.
    Here, duck typing is assumed in the sense that the empty methods here reveal the fact that this
    class is in fact acting as an interface. Python does not have interface statements as such, and
    thus all structures working as interfaces will have to be induced to be such by the user, thus
    relying on duck typing strongly.'''


class SQLreader(InformalInterfaceSQL):
    def method1(self):
        print('This object reads SQL databases')

    def method2(self):
        print('method2 shows the content of SQL databases')


class SQLwriter(InformalInterfaceSQL):
    def method1(self):
        print('This object writes into SQL databases')

    # method2 is not present in this class definition, since it shows content and the writer shouldn't
    def method3(self):
        print('method3 writes into SQL databases')


# The above defines two concrete implementations of the InformalInterfaceSQL.
# Note, however, that SQLreader implements both methods in the interface, while SQLwriter does not.
# If we now test whether these classes are subclasses of the upper interface:
print(issubclass(SQLreader, InformalInterfaceSQL))
print(issubclass(SQLwriter, InformalInterfaceSQL))
# We see that Python indeed identifies both classes as actual subclasses of the interface.
# A real interface, however, demands *by definition* that all of its stated methods be implemented
# into the classes that implement the interface. The following approach is also a form of informal
# interface, although it does exclude the case where not all interface methods are implemented in the class.

# Here you can hold on in the study of interfaces to learn about a special method which all
# classes possess. These methods are called 'dunder methods' in Python (dunder=double underscore)
# and are there to enrich the behaviour of user defined classes.
print(SQLwriter.__mro__)
print(SQLreader.__mro__)
# MRO stands for "method resolution order", and it is a very Python-specific way to handle multiple
# inheritance. If a method has been overriden several times across the parent class structure of
# a given class, the MRO shows the exact order in which the overriding has been carried out, thus
# showing which implementation of any given inherited method will be applied when called upon in
# the given class. It also provides a way to trace back a way to access earlier implementations via
# the 'super' keyword.


# Now we will fully implement an interface in Python using metaclasses.
class ExampleMeta(type):
    """ Creates a meta-class inheriting from the meta-class type. It then overrides two methods
    from its parent metaclass. This is done so that implementations of the interface (which is
    the next class defined below) are only considered as such when they implement all of the methods
    enforced by the interface."""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
        # This additional method is introduced to test instantiation via isinstance()

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'method1') and
                callable(subclass.method1) and
                hasattr(subclass, 'method2') and
                callable(subclass.method2))

class CompleteInterface(metaclass=ExampleMeta):
    """ This is actually the interface class itself. It does not feature any methods here because
    they have already been specified in the metaclass part."""
    pass

class SQLreaderNew:
    def method1(self):
        print('This object reads SQL databases')
    def method2(self):
        print('method2 shows the content of SQL databases')

class SQLwriterNew:
    def method1(self):
        print('This object writes into SQL databases')
    def method3(self):
        print('method3 writes into SQL databases')


print(issubclass(SQLreaderNew, CompleteInterface))
print(issubclass(SQLwriterNew, CompleteInterface))
# Now the second test returns false because SQLwriterNew does not implement method2
# from CompleteInterface

print(SQLreaderNew.__mro__)
print(SQLwriterNew.__mro__)
# Furthermore, these two attributes show that CompleteInterface does not feature anymore among the
# parents of these two classes. This is because it has become a virtual base class of the other two.

# The key difference between virtual classe and standard subclasses is that virtual base classes use the
# .__subclasscheck__() dunder method to implicitly check if a class is a virtual subclass of the superclass.


# ================================================================================================================
# What follows is an example of interaction between a metaclass, a base class, an informal interface via a
# virtual base class, and several child classes inheriting and implementing from the real and virtual base classes
class PersonMeta(type):
    # The metaclass
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))
                # subclasscheck is overriden and adapted for the informal interface we want to create. It checks
                # through any potential subclass of the metaclass, and it aims to test whether all our interface
                # methods are 1) accessible as attributes; and 2) callable as methods.
class PersonSuper:
    # Base class (not virtual)
    def name(self) -> str:
        pass
    def age(self) -> int:
        pass
class Person(metaclass=PersonMeta):
    # Virtual base class (the informal interface)
    pass

# Now we define two concrete classes, Employee and Friend. Employee will inherit simply from PersonSuper, the real
# base class. Friend, however, will be an implementation of the Person interface via the metaclass PersonMeta.
# Therefore, PersonSuper will appear in the MRO of Employee, while Person won't appear in the MRO of Friend.
class Employee(PersonSuper):
    pass
class Friend:
    def name(self):
        pass
    def age(self):
        pass

print(issubclass(Employee,PersonSuper))
print(issubclass(Employee,Person))
print(issubclass(Friend,PersonSuper))
print(issubclass(Friend,Person))
# Note that Employee is a subclass of Person because PersonSuper implements the methods required by the interface
# Person, but Person doesn't appear in Employee's MRO because it's a virtual class; the same goes for Friend.
print(Employee.__mro__)
print(Friend.__mro__)

# We finally try the isinstance() method to test the __instancecheck__ override we introduced in our interfaces
print(isinstance(SQLreaderNew,CompleteInterface))
print(isinstance(SQLwriterNew,CompleteInterface))
print("\n")
print(isinstance(Employee,PersonSuper))
print(isinstance(Friend,Person))
