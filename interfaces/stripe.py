import payment_gateway as pg
class StripePayment(pg.PaymentGateway):
    def initiate_payment(self, amount):
        print("This is Stripe method", amount)