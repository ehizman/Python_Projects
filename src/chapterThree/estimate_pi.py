def estimate_pi(term):
    if term < 1:
        raise ValueError("Invalid parameter!")
    elif term == 1:
        return 4
    else:
        estimate_of_pi: float = 0
        counter: int = 1
        while counter <= term:
            if counter == 1:
                estimate_of_pi = 4
            elif (counter % 2) == 0:
                estimate_of_pi -= 4 / ((2 * counter) - 1)
            else:
                estimate_of_pi += 4 / ((2 * counter) - 1)
            counter += 1
        return estimate_of_pi

