# DSA_Practice

def fac(res ,num):
    if num == 0 or num == 1:
        return 1
    
    return fac(res * num, num - 1)