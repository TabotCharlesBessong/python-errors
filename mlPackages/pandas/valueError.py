error = {ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().}
explanation = "This is just a comparison between one value and an other , rather we have series vs series comparison"
problem = {highMale : (df1['total_bill'] > 30) and (df1['sex'] == 'Male')}
solution = {highMale = (df1['total_bill'] > 30) & (df1['sex'] == 'Male')}
