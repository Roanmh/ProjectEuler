from datetime import date
print(reduce(lambda c, wd: c + (1 if wd == 6 else 0),
             (date(m // 12, (m % 12) + 1, 1).weekday()
              for m in range(1901*12, 2001*12)), 0))
