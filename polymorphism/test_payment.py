import payment as p
def test_payment():
    print()
    card = p.CardPayment()
    card.ProcessPayment()

    paypal = p.PaypalPayment()
    paypal.ProcessPayment()

def test_method_overload():
    print()
    c = p.MethodOverloadingTestClass()
    # this will raise an error if two methods are called
    # c.method_overloading(1, 2) 
    # only the calling of last method in the execution flow is expected
    c.method_overloading(1)

def test_args_method_overloading():
    print()
    c = p.MethodOverloadingTestClass()
    # same methos with different number of arguments
    c.method_overloading_with_args()
    c.method_overloading_with_args(21)
    c.method_overloading_with_args(21, 22)
    
def test_diff_datatype_method_overloading():
    print()
    c = p.MethodOverloadingTestClass()
    # in other OOP languages, the method with corresponding data type will be triggered
    # irrespective of datatype passed in args, it just triggers the last method in code flow 
    c.datatype_test(float(1.1)) # this trigger the last method : int method instead of float