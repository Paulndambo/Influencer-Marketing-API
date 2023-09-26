import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer FLWSECK-b3364a84eec61f5f1e70a2ce264f9101-18a9893e52bvt-X"
}

FLUTERWAVE_BACKEND_URL = "https://api.flutterwave.com/v3"
PAYMENT_PLANS_URL = f"{FLUTERWAVE_BACKEND_URL}/payment-plans/"

class FluterWavePaymentProcessor:
    def __init__(self):
        pass

    def get_payment_plans(self):
        res = requests.get(PAYMENT_PLANS_URL, headers=headers)
        payment_plans = res.json()

        return payment_plans
        

    def create_payment_plan(self, name, amount, currency, interval):
        self.name = name
        self.amount = amount
        self.currency = currency
        self.interval = interval

        if self.amount == 0:
            pass

        elif self.amount > 0:
            data = {
                "name": self.name,
                "amount": self.amount,
                "interval": self.interval,
                "currency": self.currency
            }
            res = requests.post(PAYMENT_PLANS_URL, data=data, headers=headers)
            
            return res.json()

    def charge_customer_card(self):
        pass

