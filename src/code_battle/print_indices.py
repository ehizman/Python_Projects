def return_indices_of_elements_that_sum_to_number_to_find(list_, number_to_find):
    dict_ = {}
    for index, element in enumerate(list_):
        remainder = number_to_find - element
        if remainder in dict_:
            return [dict_.get(remainder), index]
        else:
            dict_.update({element: index})

    return None
