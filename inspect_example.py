
class A(object):
    """The A class"""
 
    def __init__(self, name):
        self.name = name
 
    def get_name(self):
        """Return the name of instance"""
        return self.name
 
    @classmethod
    def test(cls):
        pass
 
    @staticmethod
    def do_nothing():
        pass
 
 
 
class B(A):
    """This is B class
    it is Derived from A"""
 
    # This method is not part of A
    def do_something(self):
        """Does some works"""
 
 
    def get_name(self):
        """Overrides version from A"""
        return "B(" + self.name + ")"
 
