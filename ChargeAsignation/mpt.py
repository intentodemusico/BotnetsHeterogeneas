import time

#Calculating 50000 pi decimals
def make_pi(ndecimals):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    #It's considered 10000 as the lowest decimals cuantity to measure
    #the processing capacity
    if(ndecimals<10000):
        ndecimals=50000
    for j in range(ndecimals):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2

#######################################################
##    We don't wanna print the result... Obviusly    ##
##my_array = []                                      ##
##                                                   ##
##for i in make_pi():                                ##
##    my_array.append(str(i))                        ##
##                                                   ##
##my_array = my_array[:1] + ['.'] + my_array[1:]     ##
##big_string = "".join(my_array)                     ##
##print ("here is a big string:\n %s" % big_string ) ##
#######################################################

#If you want to print the result, just use the code over this line and under
#the function definition

def calculateProcessingTime(ndecimals1):
    #Measuring time
    start = time.time()
    for i in make_pi(ndecimals1):
        pass

    #Total time
    end = time.time()
    totalTime=end - start
    #print(totalTime)
    return totalTime
