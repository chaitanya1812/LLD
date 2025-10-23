from stripe import StripePayment
from paypal import PaypalPayment
from checkout import CheckoutService
def test_stripe():
    stripe = StripePayment()
    stripe.initiate_payment(100)
def test_paypal():
    pp = PaypalPayment()
    pp.initiate_payment(125)
def test_checkout():
    pp = PaypalPayment()
    chk = CheckoutService(pp) # paypal can be the default payment gateway
    stripe = StripePayment()
    chk.set_payment_gateway(stripe) # set stripe as payment gateway

    print("proceeding to check out...")
    chk.checkout(199) # checkout via stripe


