def is_pythagoras_triple(adjacent, opposite, hypothenus) -> bool:
    max_side: int = max(adjacent, opposite, hypothenus)
    temp: int = hypothenus
    hypothenus = max_side
    if adjacent == max_side:
        adjacent = temp
    else:
        opposite = temp
    is_a_pythagoras_triple: bool = pow(hypothenus, 2) == pow(adjacent, 2) + pow(opposite, 2)
    return is_a_pythagoras_triple