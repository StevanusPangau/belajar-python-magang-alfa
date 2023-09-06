# Semua package yang kita buat dibuat dalam folder Learning

import Learning.Arithmetic as arith
import Learning.Algebra as algebra
import Learning
import sys
sys.path.append('./Learning')

Learning.foo()
Learning.do_something()

a = Learning.Computer("Macbook")
a.say_hello()

b = algebra.add(10, 5)
print(b)

c = arith.calculate(5, 8)
print(c)
