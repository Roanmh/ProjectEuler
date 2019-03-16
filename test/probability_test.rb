res = []

for i in 1..1000000
  res << 8*rand(0..1)+4*rand(0..1)+2*rand(0..1)+rand(0..1)
end

#puts res

cnt = {}

for i in 0..15
  cnt[i] = res.count(i)
end

puts cnt
