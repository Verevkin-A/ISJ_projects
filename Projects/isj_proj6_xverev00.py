#!/usr/bin/env python3

class Polynomial:
    """Polynomial class and his methods"""

    def __init__(self, *arguments, **arguments2):
        """Initialisation of object"""

        self.values = []    # initialisation of polynomial

        for i in arguments:              # if values in list format
            if isinstance(i, list):
                self.values = i

        if not self.values:
            if arguments:                # if values in format of single numbers
                self.values = list(arguments)
            else:
                for key, value in arguments2.items():      # if values in format of dictionary
                    for i in range(int(key[1:]) + 1 - len(self.values)):
                        self.values.append(0)
                    self.values[int(key[1:])] = value
            for i in range(len(self.values) - 1, 0, -1):  # removal of extra zeros
                if self.values[i] == 0:
                    del self.values[i]
                else:
                    break

    def __str__(self):
        """Method for printing polynomial in his standard format"""
        print_polynomial = ""

        if len(self.values) == 1:       # if polynomial consist of 1 number
            return str(self.values[0])

        for i in reversed(range(len(self.values))):
            if self.values[i] == 0:     # if value equals to 0, don't write it
                continue

            if print_polynomial:        # sign handling
                if self.values[i] < 0:
                    print_polynomial += " - "
                else:
                    print_polynomial += " + "

            if i == 0:                  # if it's first kf. print it without sign and 'x'
                formatted = str(abs(int((self.values[0]))))
                print_polynomial += "{}".format(formatted)
                return print_polynomial

            elif i == 1:                  # if it's second kf. print it with single 'x'
                if abs(self.values[1]) == 1:        # if abs of second kf. equals to '1', print single 'x'
                    print_polynomial += "x"
                else:
                    formatted = str(abs(int(self.values[1])))
                    print_polynomial += "{}x".format(formatted)

            else:                       # for all other kf. print them with x in right power
                if abs(self.values[i]) == 1:        # if abs of kf. equals to '1', print single 'x'
                    print_polynomial += "x^{}".format(i)
                else:
                    formatted = str(abs(int(self.values[i])))
                    print_polynomial += "{}x^{}".format(formatted, i)
        return print_polynomial

    def __eq__(self, other):
        """Check for equality of two polynomials"""
        if len(other.values) != len(self.values):       # check for equal length of 2 polynomials
            return False
        for first, second in zip(other.values, self.values):        # compare each kf. of 2 polynomials
            if first != second:
                return False
        return True         # return 'True' in case of equal polynomials

    def __add__(self, other):
        """Addition of two polynomials"""
        n = 0
        answer = self.values.copy()         # set output polynomial

        for first, second in zip(self.values, other.values):        # add two polynomials
            answer[n] = first + second
            n += 1
        if len(other.values) > len(self.values):        # if 1 polynomial > 2, add remain values
            for i in range(len(self.values), len(other.values)):
                answer.append(other.values[i])
        return Polynomial(answer)       # return answer in different polynomial

    def __mul__(self, other):           # help method for raise in power
        """Multiplication of 2 polynomials"""
        answer = (len(self.values) + 1 + len(other.values)) * [0]       # allocate places for answer
        for i in range(len(self.values)):
            for j in range(len(other.values)):
                answer[j + i] += other.values[j] * self.values[i]
        return Polynomial(answer)

    def __pow__(self, power):
        """Raise polynomial in given power"""
        if power < 0:       # raise error if power is negative number
            raise ValueError("Power number mustn't be negative")
        elif power == 0:    # if power equals zero answer always '1'
            return 1
        elif power == 1:        # return same polynomial if power equals 1
            return Polynomial(self.values)
        elif power > 1:         # in other cases multiply Polynomial by himself x times
            answer = self
            for _ in range(1, power):
                answer *= self
            return Polynomial(answer)

    def derivative(self):
        """Derivation of the polynomial"""
        if len(self.values) == 1:       # if polynomial consist of 1 number return zero
            return 0
        answer = self.values[1:]        # allocate answer variable
        for i in range(len(answer)):        # count derivative
            answer[i] *= (i + 1)
        return Polynomial(answer)

    def at_value(self, a, *b):
        """Calculate polynomial with given value(s)"""
        answer, answer2 = 0, 0      # set variables for answer
        for index, value in enumerate(self.values):     # count first value
            addition = (a ** index) * value
            answer += addition
        if b:                   # count second value, if exist
            for index, value in enumerate(self.values):
                addition = (b[0] ** index) * value
                answer2 += addition
            answer = answer2 - answer
        return answer
