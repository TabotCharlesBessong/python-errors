#The Python "ValueError: invalid literal for int() with base 10" occurs when we pass a string that cannot be directly converted to an integer (e.g. an empty string or a float) to the int() class. To solve the error, convert the string to a float first, e.g. int(float(my_str)) .

error = {intTemp : int(row[1])}
solution = {intTemp:int(float(row[1]))}

# The error above sometimes happens when you are trying convert list of element into a form and some values cannot be tycast
# for example it having some string string value instead of string num values
# example
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny

# In the first column , we have real string and not just numbers which can be strings 

# so the best solution is shown below
for row in d:
    if row[1] != 'temp':
      intTemp = int(row[1])
      temperatures.append(intTemp)
  print(temperatures)
