def count_facs(num)
  count = 0
  for i in 1..Math.sqrt(num).floor
    count += 2 if num % i == 0
  end
  return count
end

def brute(num, facs)
  i = 1
  sum = 1

  while true
    i += 1
    sum += i
    puts i.to_s + " " + sum.to_s
    return sum if count_facs(sum) > 500
  end
end

print brute(6,500)