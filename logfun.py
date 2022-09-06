import numpy as np
def logfun(x,r,l):
    output = [x,]
    for e in np.arange(1,l):
        output_e = r*output[e-1]*(1-output[e-1])
        output.append(output_e)
    return output[-1]

print(logfun(0.1,2,2))