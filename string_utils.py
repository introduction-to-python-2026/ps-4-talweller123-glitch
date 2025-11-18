def split_at_first_digit(formula):
    first_digit_index = -1
    for i, char in enumerate(formula):
        if char.isdigit():
            first_digit_index = i
            break         
    if first_digit_index == -1:
        return (formula, 1)         
    else:
        prefix = formula[:first_digit_index]
        number_str = formula[first_digit_index:]
        number_int = int(number_str)        
        return (prefix, number_int)
def split_before_each_uppercase(formula):
    results = []
    current_segment = ""  
    for char in formula:
        if char.isupper() and current_segment:
            results.append(current_segment)
            current_segment = char
        else:
            current_segment += char            
    if current_segment:
        results.append(current_segment)        
    return results
