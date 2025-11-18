def split_before_each_uppercases(formula: str):
    if formula == "":
        return []

    parts = []
    current = ""

    for ch in formula:
        if ch.isupper():
            if current:
                parts.append(current)
            current = ch
        else:
            current += ch

    if current:
        parts.append(current)
    return parts


def split_at_first_digit(formula: str):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return(formula,1)
