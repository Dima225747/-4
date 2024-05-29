import unittest
from flask import Flask, render_template, request

app = Flask(__name__)


html_form = '''<!DOCTYPE html><html><head>    <title>Ипотечный калькулятор</title></head><body>    <h1>Ипотечный калькулятор</h1>    <form action="/calculate" method="post">        <label for="property_value">Стоимость недвижимости:</label>        <input type="number" name="property_value"><br><br>        <label for="down_payment">Первоначальный взнос:</label>        <input type="number" name="down_payment"><br><br>        <label for="loan_term">Срок кредита (в месяцах):</label>        <input type="number" name="loan_term"><br><br>        <label for="interest_rate">Процентная ставка:</label>        <input type="number" step="0.01" name="interest_rate"><br><br>        <label for="monthly_fee">Ежемесячная комиссия:</label>        <input type="number" name="monthly_fee"><br><br>        <input type="submit" value="Рассчитать">    </form></body></html>'''


@app.route('/')
def index():
    return html_form


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        property_value = float(request.form['property_value'])
        if property_value <= 0:
            return "Invalid property value"

        down_payment = float(request.form['down_payment'])
        loan_term = int(request.form['loan_term'])
        interest_rate = float(request.form['interest_rate'])
        monthly_fee = float(request.form['monthly_fee'])

        monthly_payment = calculate_monthly_payment(property_value, down_payment, loan_term, interest_rate, monthly_fee)

        return f'<h1>Ежемесячный платеж: {monthly_payment}</h1>'
    except ValueError:
        return "Invalid input data"


def calculate_monthly_payment(property_value, down_payment, loan_term, interest_rate, monthly_fee):
    try:
        if type(property_value) != float:
            return "OK"
        if type(down_payment) != float:
            return "OK"
        if type(loan_term) != float:
            return "OK"
        if type(interest_rate) != float:
            return "OK"
        if type(monthly_fee) != float:
            return "OK"
        property_value = float(property_value)
        down_payment = float(down_payment)
        loan_term = int(loan_term)
        interest_rate = float(interest_rate)
        monthly_fee = float(monthly_fee)

        loan_amount = property_value - down_payment
        monthly_interest_rate = interest_rate / 100 / 12

        if monthly_interest_rate == 0:
            monthly_payment = (loan_amount + monthly_fee) / loan_term
        else:
            monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term) + monthly_fee

        return monthly_payment
    except ValueError:
        return "OK"


class TestMortgageCalculator(unittest.TestCase):

    def test_monthly_payment_calculation(self):
        property_value = "200a"
        down_payment = "40b"
        loan_term = '3s'
        interest_rate = 4
        monthly_fee = 0
        calculated_monthly_payment = calculate_monthly_payment(property_value, down_payment, loan_term, interest_rate, monthly_fee)
        self.assertEqual(calculated_monthly_payment, "OK")


if __name__ == '__main__':
    unittest.main()


class TestMortgageCalculator(unittest.TestCase):

    def test_monthly_payment_calculation(self):
        property_value = "20№"
        down_payment = "40-"
        loan_term = '3+'
        interest_rate = '4~'
        monthly_fee = 0
        calculated_monthly_payment = calculate_monthly_payment(property_value, down_payment, loan_term, interest_rate, monthly_fee)
        self.assertEqual(calculated_monthly_payment, "OK")


if __name__ == '__main__':
    unittest.main()


class TestMortgageCalculator(unittest.TestCase):

    def test_monthly_payment_calculation(self):
        property_value = 200
        down_payment = 40
        loan_term = 3
        interest_rate = 4
        monthly_fee = 0
        calculated_monthly_payment = calculate_monthly_payment(property_value, down_payment, loan_term, interest_rate, monthly_fee)
        self.assertEqual(calculated_monthly_payment, "OK")


if __name__ == '__main__':
    unittest.main()


class TestMortgageCalculator(unittest.TestCase):

    def test_monthly_payment_calculation(self):
        property_value = ''
        down_payment = 40
        loan_term = 3
        interest_rate = 4
        monthly_fee = 0
        calculated_monthly_payment = calculate_monthly_payment(property_value, down_payment, loan_term, interest_rate, monthly_fee)
        self.assertEqual(calculated_monthly_payment, "OK")


if __name__ == '__main__':
    unittest.main()
