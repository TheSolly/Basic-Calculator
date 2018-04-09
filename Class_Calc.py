class Calculator:
    def __init__(self, oprType, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.oprType = oprType

    def operations(self):
        if self.oprType == 1:
            self.add(self.num1, self.num2)
        if self.oprType == 2:
            self.sub(self.num1, self.num2)
        if self.oprType == 3:
            self.mult(self.num1, self.num2)
        if self.oprType == 4:
            self.div(self.num1, self.num2)

    def add(self, num1, num2):
        print 'Adding = ', num1 + num2

    def sub(self, num1, num2):
        print 'Substracting = ', num1 - num2

    def mult(self, num1, num2):
        print 'Multiplying = ', num1 * num2

    def div(self, num1, num2):
        try:
            print 'Dividing = ', num1 / num2
        except(ZeroDivisionError):
            print "Division by Zero error"
