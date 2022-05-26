import pandas as pd  
  
# string values in the list   
lst = ['Java', 'Python', 'C', 'C++',  
         'JavaScript', 'Swift', 'Go']  
  
# Calling DataFrame constructor on list  
dframe = pd.DataFrame(lst)  
print(dframe)  