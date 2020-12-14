class Rational:
    def __init__(self, n, m):
        self.numerator = n
        self.denominator = m
        self.Rational = (self.numerator, self.denominator)

    def summ(self, y):
        res_numerator = self.numerator*y.denominator+y.numerator*self.denominator
        res_denominator = self.denominator*y.denominator
        print((res_numerator, res_denominator))

    def sub(self, y):
        res_numerator = self.numerator*y.denominator-y.numerator*self.denominator
        res_denominator = self.denominator*y.denominator
        print((res_numerator, res_denominator))

    def mult(self, y):
        res_numerator = self.numerator*y.numerator
        res_denominator = self.denominator*y.denominator
        print((res_numerator, res_denominator))

    def div(self, y):
        res_numerator = self.numerator*y.denominator
        res_denominator = self.denominator*y.numerator
        print((res_numerator, res_denominator))
    
    def from_ration_to_float(self):
        print(self.numerator/self.denominator)
    
    @classmethod
    def get_rational_from_string(cls, string):
        inputed_number = string.split('/')
        return(Rational(int(inputed_number[0]), int(inputed_number[1])))
        



def test_operations(): 
    x = Rational(1, 2)
    y = Rational(1, 2)
    
    print(x.Rational)
    print(y.Rational)
    x.summ(y)
    x.sub(y)
    x.mult(y)
    x.div(y)

def test_cast_to_float():
    z = Rational(1, 4)
    z.from_ration_to_float()


def test_parse_from_string():
    inputed_number = '235/705'

    x = Rational.get_rational_from_string(inputed_number)
    print(x.Rational)


if __name__ == '__main__':
    test_operations()
    test_cast_to_float()
    test_parse_from_string()
