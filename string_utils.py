def split_all_words_and_digits(formula):
    results = []
    current_segment = ""

    is_digit_prev = None 

    for char in formula:
        is_digit_current = char.isdigit()
        
    
        if current_segment and is_digit_current != is_digit_prev:          
            results.append(current_segment)
            current_segment = char
        else:
            current_segment += char

        is_digit_prev = is_digit_current
        
    if current_segment:
        results.append(current_segment)
        
    return results

formula_a = "Ir6"
print(split_all_words_and_digits(formula_a))  

formula_b = "H2SO4"
print(split_all_words_and_digits(formula_b)) 

formula_c = "C6H12O6"
print(split_all_words_and_digits(formula_c))  


def split_at_first_digit(formula):
    pass # Replace the `pass` with your code
