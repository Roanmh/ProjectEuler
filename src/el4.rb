# Problem: largest palindromic product of two 3 digit factors include

#require 'math'

# Separates number into each base 10 digit
# Validated, not optimized
def to_a (num)
  arr = []
  for i in Math.log10(num).floor.downto(0) # Range for separating each digit
    arr.push((num/10**i).floor - (num/10**(i+1)).floor * 10 )
  end
  return arr
end

def p_check (num)
  arr = to_a(num)
  for i in 0...(arr.length/2)
    c1 = arr[i]
    c2 = arr[arr.length - i - 1]
    if c1 != c2
      return false
    end
  end
  return true
end


def basic(num)
  high_p = 0
  for i in 1..num
    for j in 1..i
      prod = i*j
      high_p = prod if p_check(i*j) and high_p < prod
    end
  end
  return high_p
end

res = basic(999)
print res