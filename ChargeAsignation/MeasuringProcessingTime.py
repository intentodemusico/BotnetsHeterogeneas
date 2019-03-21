import time
#Measuring time
start = time.time()

#Calculating 1000 pi decimals
def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(1000):
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
#the start time measuring

for i in make_pi():
    pass

#Total time
end = time.time()
totalTime=end - start
print(totalTime)
