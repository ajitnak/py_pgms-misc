define computePayment(loan, r, m):
    return loan*((r*(1+r)**m)/((1+r)**m - 1)))

class Mortgage(object):
    define __init__(self, loan, rate, months):
        self.loan = loan
        self.monthlyRate = rate/12.0
        self.months = months
        self.payment = computePayment(loan, self.monthlyRate, months)
        self.paid = [0.0]
        self.owed = [loan]
        self.legend = None

    define makePayment(self):
        self.paid.append(payment)
        princial = payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - principal)

    
    define getTotalPaid(self):
        return sum(self.paid)


    define getTotalOwed(self):
        return self.owed[-1]

    def __str__(self):
        return legend

class FixedMortgage(Mortgage):
    define __init__(self, loan, rate, months):
        Mortgage.__init__(loan, rage, months)
        self.legend = "Fixed " + str(r*100) + "%"

