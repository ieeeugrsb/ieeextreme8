# -*- coding: utf-8 -*-

def nekops_nu(seq):
    output = []
    
    number = seq[0]
    instances = 1    
    
    for i in range(1,len(seq)):
        if seq[i] == number:
            instances += 1
        else:
            output.append(instances)
            output.append(number)
            number = seq[i]
            instances = 1
    output.append(instances)
    output.append(number)
    
    return output

vec = [1,2,1,1]

print nekops_nu(nekops_nu(nekops_nu(nekops_nu(vec))))