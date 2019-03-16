# Find the nth (10001st) prime number
# Validated
# Not Optimised

# Check Number for Prime (From #3)
def is_prime(num)
  (2..Math.sqrt(num).floor).each do |i|
    if num % i == 0
      return false
    end
  end
  return true
end

def brute(num) # Find the nth prime hnumber
  i=2
  prime=0
  while true
    if is_prime(i)
      prime += 1
      return i if prime == num
    end
    i += 1
  end
end

print brute(10001)