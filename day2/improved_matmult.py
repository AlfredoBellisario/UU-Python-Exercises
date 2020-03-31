import numpy

N = 250


X = numpy.random.randint(0, 100, size = (N,N))
Y = numpy.random.randint(0, 100, size = (N,N+1))

Z = numpy.dot(X,Y)
result = Z.tolist()
    
for r in result:
    print(r)


