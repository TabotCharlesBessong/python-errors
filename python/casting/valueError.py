#The Python "ValueError: invalid literal for int() with base 10" occurs when we pass a string that cannot be directly converted to an integer (e.g. an empty string or a float) to the int() class. To solve the error, convert the string to a float first, e.g. int(float(my_str)) .

error = {intTemp : int(row[1])}
solution = {intTemp:int(float(row[1]))}
