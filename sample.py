class MyClass(object):
    '''
    Simple class with addition functions to provide examples for testing.
    '''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2


    def add_only_positive(self):
        if self.num1 > 0 and self.num2 > 0:
            return self.num1 + self.num2
        else:
            return None
