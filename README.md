# project-euler
Solutions for project euler


- [ ] Add benchmark for the different languages
- [ ] Optimize
- [ ] Create excel to get average performance
- [ ] How to benchmark for Go and Python?

Version: macOS Sierra, Version 10.12.3
Machine:
MacBook Pro (13-inch, 2016, Four Thunderbolt 3 Ports)
Processor: 2.9 GHz Intel Core i5
Memory: 8 GB 2133 MHz LPDDR3
Graphics: Intel Iris Graphics 550 1536 MB

| - | Python | Golang |
|--|--|--| 
| 1 | 0.000236 s | 0.00000571 |
| 2 | 3.09586524963e-05 s | |
| 3 | |
| 4 | |
| 5 | 0.569571700096 s | 0.028574718 s |
| 6 | 0.507622 s |  | 
| 7 | 1.293534 s | | 
| 8 | 1.38282775879e-07 s |  | 
| 9 | 0.49537498951 s | | 
| 10 | 107.232675409 s | | 
| 11 | 0.000911300182343 s |  | 
| 12 | 4.61435410976 s |  | 
| 13 | 0.000177693367004 s| | 
| 14 | 45.7734566927 s |  | 
| 15 |  2.96521186829e-05 |  | 
| 16 |  0.000258100032806 s |  | 
| 17 | 0.00495417833328 s | | 
| 18 | 0.00125045061111 s | | 
| 19 |  0.00124981880188 s |  | 
| 20 |  0.000204420089722 s |  | 
| 21 | 7.27057590485 s | | 
| 22 | 0.0189262080193 s | | 
| 23 | Too long ...  |  | 
| 24 |  0.000128602981567 s | | 
| 25 | 0.0274871897697 s | | 
| 26 | - | - |
| 27 |  11.2318995953 s |  | 
| 28 | 38.9268630028 s |  | 
| 29 | 0.0228111982346 s | | 
| 30 | Too long |  | 
| 31 | - | - |
| 32 | Too long...| | 
| 33 | 0.0168312072754 s |  | 
| 34 | 6.25762090683 s | | 
| 35 | Too long...| | 
| 36 |  0.949850916862 s  | | 
| 37 | 0.000824189186096 s | | 
| 38 | 0.985824799538 s | | 
| 39 |  0.572762703896 s | | 
| 40 | 0.0954653024673 s | | 
| 41 | | | 
| 42 | | | 
| 43 | | | 
| 44 | | | 
| 45 | | | 
| 46 | | | 
| 47 | | | 
| 48 | | | 
| 49 | | | 
| 50 | | | 


# Python

The solutions for the python codes are placed in the python folder.
Benchmarking a function is easy - just add the following line at the end of each file:
```python
if __name__ == '__main__':
    import timeit
    ITERATIONS = 1000 # For longer running functions, you can reduce it
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
```

Note that the `number` refers to the number of times the function will be called to carry out the benchmark. We divide the the time taken by 1000 to get the average time.