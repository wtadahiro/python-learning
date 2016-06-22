class BasicSyntaxes:
    def over10(self, num):
        if num > 10:
            return True
        else:
            return False

    def fizzbuzz(self, num):
        if num <= 0:
            raise Exception()

        if num % 15 == 0:
            return 'fizzbuzz'
        elif num % 5 == 0:
            return 'buzz'
        elif num % 3 == 0:
            return 'fizz'
        else:
            return None

    def square_list(self, in_list):
        out_list = []
        for val in in_list:
            out_list.append(val**2)
        return out_list


