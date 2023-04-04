# Our starting values
term1 = 0
term2 = 1
count = 0
total_terms = 100

# Loop until we hit our total
while count < total_terms:
    print(term1)
    
    # Update the value with each cycle
    next_term = term1 + term2
    term1 = term2
    term2 = next_term
    count = count + 1