principal = 10000     
annual_rate = 0.05    
years = 3            
compound_value= principal * (1 + annual_rate) ** years
simple_value=principal*(1+annual_rate*years)
print(round(simple_value, 2))
print(round(compound_value, 2))
print(round(compound_value - simple_value, 2))