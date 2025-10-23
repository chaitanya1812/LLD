import payment_gateway as pg
class CheckoutService():
    def __init__(self, pg : pg.PaymentGateway):
        self.payment_gateway = pg
    def set_payment_gateway(self, pg):
        self.payment_gateway = pg
    # check out service doesn't care about the type of payment gateway
    def checkout(self, amount):
        self.payment_gateway.initiate_payment(amount)