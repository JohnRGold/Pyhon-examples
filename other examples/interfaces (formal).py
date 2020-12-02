""" To enforce the subclass instantiation of abstract methods, we utilize Python’s builtin
ABCMeta from the abc module. Rather than create our own metaclass (like we did for informal interfaces,
we use abc.ABCMeta as the metaclass. Then, we overwrite .__subclasshook__() in place of .__instancecheck__()
and .__subclasscheck__(), as it creates a more reliable implementation of the dunder methods used in
informal interfaces."""

import abc

class myFormalInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'method1') and
                callable(subclass.method1) and
                hasattr(subclass, 'method2') and
                callable(subclass.method2))

class SQLreaderFormal:
    def method1(self):
        pass
    def method2(self):
        pass
class SQLwriterFormal:
    def method1(self):
        pass
    def method3(self):
        pass
print(issubclass(SQLreaderFormal,myFormalInterface)) # returns True
print(issubclass(SQLwriterFormal,myFormalInterface)) # returns False

# ===========================================================================================

# Now we can register a virtual subclass using the .register() meta-method,
# hence registering Double as a virtual subclass of float.
class Double(metaclass=abc.ABCMeta):
    pass
Double.register(float)

print(issubclass(float, Double))
print(isinstance(1.234, Double))
# Both return true

@Double.register
class Double64(Double):
    pass
print(issubclass(Double64, Double)) # Returns true as well

''' However, using subclass detection with registration, one must be 
careful when combining .__subclasshook__() and .register().
To ensure that the registered virtual subclasses are taken
into consideration, one must add NotImplemented to the
.__subclasshook__() dunder method. The myFormalInterface
would be updated to the following: '''
class myFormalInterface2(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'method1') and
                callable(subclass.method1) and
                hasattr(subclass, 'method2') and
                callable(subclass.method2) or
                NotImplemented)
class SQLreaderFormal2:
    def method1(self):
        pass
    def method2(self):
        pass
@myFormalInterface2.register
class SQLwriterFormal2:
    def method1(self):
        pass
    def method3(self):
        pass

print(issubclass(SQLreaderFormal2, myFormalInterface2))
print(issubclass(SQLwriterFormal2, myFormalInterface2))
''' Even if SQLwriterFormal2 doesn't override method2, it is
still marked as a virtual subclass of myFormalInterface2,
and thus an implementation of myFormalInterface2.
This is why caution is strongly advised to be cautious
when handlnig virtual subclass registration. '''

# ========================================================================

''' We can now use abstract method declaration.
An abstract method is a method declared by the Python 
interface, but it may not have a useful implementation. The abstract 
method must be overridden by the concrete class that implements 
the interface in question.
To create abstract methods in Python, we add the @abc.abstractmethod 
decorator to the interface’s methods. In the next example, we update 
the myFormalInterface to include the abstract methods 
.method1() and .method2()'''
class myFormalInterface3(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'method1') and
                callable(subclass.method1) and
                hasattr(subclass, 'method2') and
                callable(subclass.method2) or
                NotImplemented)
    @abc.abstractmethod
    def method1(self):
        raise NotImplementedError
    @abc.abstractmethod
    def method2(self):
        raise NotImplementedError
class SQLreaderFormal3(myFormalInterface3):
    def method1(self):
        pass
    def method2(self):
        pass
class SQLwriterFormal3(myFormalInterface3):
    def method1(self):
        pass
    def method3(self):
        pass
    ''' This formal interface will raise errors when the abstract
    methods aren't overridden. The SQLreaderFormal3
    instance, sql_reader, won't raise any errors,
    as SQLreaderFormal3 is correctly overriding the SQLreaderFormal3
    abstract methods. However, sql_writer will raise an error: '''
sql_reader = SQLreaderFormal3()
sql_writer = SQLwriterFormal3()
