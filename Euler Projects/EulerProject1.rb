# Author: Roan Martin-Hayden
# Description: Code to complete Euler Project 1
# Date: 11/5/2015

#Initial variables. Defined as variables for ability for flexibility
a = 1
b = 1000
total = 0

# For each loop from 1-999
(a...b).each { |i|
  # Test i for multiple of 3 and 5
  if i % 3 == 0 or i % 5 == 0
    # Add to the su if so
    total += i
  end
}

#Print total
print 'Total: ', total, "\n"