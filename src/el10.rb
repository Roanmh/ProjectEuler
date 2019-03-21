# Check Number for Prime
def is_prime(num)
  (2..Math.sqrt(num).floor).each do |i|
    if num % i == 0
      return false
    end
  end
  return true
end

def brute(num)
  total = 0
  (2...num).each do |i|
    total += i if is_prime(i)
  end
  return total
end

print brute(10)
print brute(2000000)