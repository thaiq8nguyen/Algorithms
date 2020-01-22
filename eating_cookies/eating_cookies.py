#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n <= 1:
    return 1
  else:
    ways_to_eat = 0
  for i in range(1, min(n+1,4)):
    ways_to_eat += eating_cookies(n - i)
  
  return ways_to_eat
  
  

print(eating_cookies(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')