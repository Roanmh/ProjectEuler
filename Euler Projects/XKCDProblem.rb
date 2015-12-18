# print "This calculator will find all of the values of a,b that satisfy a*sqrt(b)=b/a\nEnter a start value for a: "
# a1 = gets.to_i
# print 'Enter a stop value for a: '
# a2 = gets.to_i
# print 'Enter a start value for b: '
# b1 = gets.to_i
# print 'Enter a stop value for b: '
# b2 = gets.to_i

a1, a2 = 1, 100
b1, b2 = a1**4, a2**4

sol = []

for a in a1..a2
  for b in b1..b2
    # print a*Math.sqrt(b)
    # print "\t"
    # puts b/a
    if a*Math.sqrt(b) == b/a
      sol << [a, b, b/a]
    end
  end
end

print sol