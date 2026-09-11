def simpleInterest(principal, rate, time):
    """
    Calculate simple interest.
    
    Args:
        principal (float): Principal amount.
        rate (float): Interest rate.
        time (float): Time in years.
        
        logic: (principal * rate * time) / 100
        formula: P * R * T / 100 -> 100 * 10 * 1 / 100 
        calculation:
        100 * 10 * 1 = 1000
        1000 / 100 = 10
        
    Returns:
        float: Simple interest.
    """
    return (principal * rate * time) / 100

print(simpleInterest(100, 10, 1)) # output: 10.0
