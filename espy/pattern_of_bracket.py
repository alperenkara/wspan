def bracket_pattern(input_str):
    # Number of opening and closing brackets are equal.
    count_closing = input_str.count(')')
    opening_closing = input_str.count('(')
    if count_closing != opening_closing:
        return False
    # Pattern should not start with closing bracket and end with opening bracket.
    elif input_str.startswith(')'):
        return False
    elif input_str.endswith('('):
        return False
    else:
        return True
    
	

    
input_str="(())("
print(bracket_pattern(input_str))