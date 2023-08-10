""""
Module will run time tests in nanoseconds for the execution times of fibonacci.py 
Yvonne Cheng 
csci 112
Winter, 2023
"""
import time
import fibonacci
import matplotlib.pyplot as plot

#Calculate execution time in exponential time(ns)
def exp_time(n):
    start = time.process_time_ns()
    fibonacci.powexponential(n)
    end = time.process_time_ns()
    return end - start
#Calculate execution time in linear time(ns) 
def linear_time(n):
    start = time.process_time_ns()
    fibonacci.powlinear(n)
    end = time.process_time_ns()
    return end - start
#Calculate execution time in logarithmis time(ns) 
def log_time(n):
    start = time.process_time_ns()
    fibonacci.powlog(n)
    end = time.process_time_ns()
    return end - start

if __name__ == '__main__':
    input_sizes = [0, 10, 20, 30, 40, 50]
    for n in input_sizes:
        print("exp_time({}) took {} ns".format(n, exp_time(n)))
        print("linear_time({}) took {} ns".format(n, linear_time(n)))
        print("log_time({}) took {} ns".format(n, log_time(n)))


 


