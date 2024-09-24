def typeChecker(i):
    if type(i) == int:
       float_value =  float(i)
       return {'val': float_value , 'type': type(float_value)}
    else:
        return {'val': i , 'type': type(i)}

print(typeChecker(2))
print(typeChecker('22'))