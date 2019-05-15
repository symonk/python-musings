

class TypesOfMethods:

    def instance_method(self):
        # instance methods require 'self' and are the run of the mill method, scoped to an instance of the class
        # instance methods require an instance of the class to be invoked
        # each instance of the class is calling its very own, 'instance_method()'
        raise NotImplementedError

    @staticmethod
    def static_method():
        # static methods do not require any instance of the class and as such, do not require an explicit 'self' arg
        # static methods are decorated with the @staticmethod decorator
        # all instances of the class use the very same static method
        # static methods cannot directly access instance methods or instance variables
        # totally self contained, but can access other static vars and methods
        raise NotImplementedError

    @classmethod
    def class_method(cls):
        # class methods require 'cls' and are
        # class methods do not know about instance methods or instance variables
        # class methods can call other static methods
        # class methods can manipulate the class itself
        raise NotImplementedError


TypesOfMethods.class_method()  # call a class method without an instance!
TypesOfMethods.static_method()  # call a static method without an instance!
TypesOfMethods.instance_method()  # call an instance method without an instance, uh oh won't work!
