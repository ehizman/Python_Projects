def return_indices_of_elements_that_sum_to_number_to_find(list_, number_to_find):
    dict_ = {}
    for index in range(len(list_)):
        remainder = number_to_find - list_[index]
        if remainder in dict_:
            return [dict_.get(remainder), index]
        else:
            dict_.update({list_[index]: index})

    return None
