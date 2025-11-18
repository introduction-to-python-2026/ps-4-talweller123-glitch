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
    if not formula:
        return []        
    results = []
    current_element = formula[0]     
    for char in formula[1:]:
        if char.isupper():
            results.append(current_element)
            current_element = char
        else:
            current_element += char            
    if current_element:
        results.append(current_element)       
    return results
