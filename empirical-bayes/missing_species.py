import pandas as pd
df = pd.read_table('https://web.stanford.edu/~hastie/CASI_files/DATA/butterfly.txt', sep=' ')

def missing_species(observation, t):
    '''
    The six lines of code to replicate the missing species problem.  
    
    Comment: Clearly this fails for t>1.  Doesn't it also seems to fail at t==1?  
    '''
    
    expected_value = 0
    
    for number, value in enumerate(observation):
        sign = 1    
        if (number+1) % 2 == 0: 
            sign = sign * -1        
        expected_value =  expected_value + sign * (value * t**(number+1))

    
    return expected_value
missing_species(df['y'], 0.5)
## 45.17
