# Author: Roan Martin-Hayden
# Description: Code to complete Euler Project 2
# Date: 11/5/2015

# variables set up. Made variables for flexibilty
stop = 4000000
total = 0

# variables to initiate and carry out fib seq
i = 1
j = 1

# while loop will continue until stop value
while j <= stop
  # single Progression of fib seq. t is a temp holder for during generation of new j value.
  t = j
  j += i
  i = t

  # if new val is even then add to total
  if j % 2 == 0
    total += j
  end
end


print 'Total: ', total, "\n"