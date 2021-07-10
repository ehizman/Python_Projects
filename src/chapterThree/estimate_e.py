def find_estimate_of_e_for_nth_term(term):
    if term == 1:
        return 1
    else:
        denominator: int = term - 1
        estimate_of_e: float = 0
        factorial: int = 1
        while denominator >= 1:
            count: int = denominator
            while count > 1:
                factorial *= count
                count -= 1
            estimate_of_e += 1 / factorial
            factorial = 1
            denominator -= 1
        return estimate_of_e + 1
