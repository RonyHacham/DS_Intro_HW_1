def my_func(x1,x2,x3):
    if((type(x1)!=float) or (type(x2)!=float) or (type(x3)!=float)):
        return ("Error: parameters should be float")
    if ((x1+x2+x3)==0):
        return ("Not a number – denominator equals zero")
    func=((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
    return (float(func))


def convert(hours, minutes):
    if ((type(hours)==str) or(type(minutes)==str)):
        return ("Input error!")
    if ((hours<0) or (minutes<0)):
        return ("Input error!")
    solu= (hours*60*60)+(minutes*60)
    return (solu)


