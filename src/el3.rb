# Author: Roan Martin-Hayden
# Description: Code to complete Euler Project 2
# Date: 11/5/2015

require 'benchmark'

# Variables for run of test
test_num = 600851475143

# Check Number for Prime
def is_prime(num)
  (2..Math.sqrt(num).floor).each do |i|
    if num % i == 0
      return false
    end
  end
  return true
end

# SLOW A.F. (Haven't seen it finish @ euler number)
def high_prime_fac (num)
  # Set up first possible factor as half the number
  factor = num/2.floor

  puts 'Starting Test'

  while factor > 1 # Run Until last possible factor
    #print factor, ": "
    # Optimization: Switch to check prime first? (I thought this would be faster)
    if (num % factor == 0) then # Check if factor
      # print "\tf"
      print "\n", factor, ":\tf"
      if is_prime(factor) then # Check if prime
        print "\tp\n\nPrime is: ", factor, "\n\nExiting...\n"
        return factor
      end
    end
    factor -= 1 # Next possible factor
  end
  return -1 # Return error value
end

def prime_fac_2 (num)
  div = 2 # Initial divisor
  div_high = 2 # Holder for highest divisor
  fac = num.to_f / div # Factor found from dividing div from the number (setting up for loop here)

  while fac >= div # Perform loop while factor is less than the divisor (essentially sqrt of num)
    if fac % 1 == 0 # if the factor is natural ...
      if is_prime(fac) # if the factor is prime
        return fac # factor will decrease every round, so you can take the value regardless (RIGHT?)
      elsif is_prime(div) # check if the divisor itself is prime
        div_high = div # store because it's the highest yet of the divisors
      end
    end

    div += 1 # Add to the divisor for next check
    fac = num.to_f / div # Update fac value
  end
  return div_high # Return highest divisor because no higher factor was found

end


puts Benchmark.measure { prime_fac_2(test_num) }