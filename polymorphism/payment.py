class PaymentProcessor:
    # check method overriding in child classes
    def ProcessPayment(self):
        print("Base class...")

# similar approach works for abstract classes as well.

class CardPayment(PaymentProcessor):
    # override method
    def ProcessPayment(self):
        print("payment processing...card payment")
    
class PaypalPayment(PaymentProcessor):
    # override method
    def ProcessPayment(self):
        print("payment processing...paypal payment")
    
# test class for method overloading - last method in code flow overrides previous methods
class MethodOverloadingTestClass():
    
    def method_overloading(self, a:int, b:int):
        print("method overloading with 2 args : ", a, b)
    
    # only the latest method is considered, all the previous methods with same names are ignored
    def method_overloading(self, a:int):
        print("method overloading with 1 arg : ", a)
    
    # kind of method overloading with any number of args:
    def method_overloading_with_args(self, *args):
        if len(args) == 0:
            # implementation with no args
            print("no args provided")
        elif len(args) == 1:
            # implementation with one args
            print("one arg : ", args[0])
        else:
            # implementation with more than one args
            print("more than one arg : ", args)
    
    # in other OOP languages, the method with corresponding data type will be triggered
    def datatype_test(self, a: float):
        print("float data type method", a)

    # in python the last method in the code flow will be triggered irrespective of the datatypes passed in args
    def datatype_test(self, a: int):
        print("int data type method", a)
    
    




    

    

    
    
    


    