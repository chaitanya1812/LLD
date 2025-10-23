import payment_gateway as pg

class PaypalPayment(pg.PaymentGateway):
    def initiate_payment(self, amount):
        print("This is Paypal gateway", amount)