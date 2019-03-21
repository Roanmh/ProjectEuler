#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#needed factors 11-20 (based on el\ iminating multiples)

FACS = 11..20
HIGH_GUESS = 670442572800

def mult(num)
  FACS.each() { |i| return false if num % i == 0 }
  return true
end

def brute(num)
  num.step(20,-20) do |i|
    return i if mult(i)
  end
  return "Well, shit..."
end

print brute(HIGH_GUESS)


