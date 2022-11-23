errors = [
  {error1:"AttributeError: 'NoneType' object has no attribute 'drop'"},
  problem:{df3 : df2.drop(['tip-percentage'],axis=1,inplace=True)},
  explanation:"df.drop does not return anything when inplace is set to True. It modifies the DataFrame in place and returns None. You don't need to create new names for them."}
  solution:{df3 : df2.drop(['tip-percentage'],axis=1,inplace=True)}
]
