# pool_ops.py
# cd Desktop\Phyton
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
#  Example: python3 pool_ops.py 4 28 28 2 2 2 0
#  4
#  14
#  14
#  2352
#  0
#  784
#
# Parameters:
#  c_in: input channel count
#  h_in: input height count
#  w_in: input width count
#  h_pool: number of filters in the convolution layer
#  w_pool: filter height count
#  s: stride of convolution filters
#  p: amount of padding on each of the four input map sides
#  ...
# Output:
#  print(int(c_out)) # output channel count
#  print(int(h_out)) # output height count
#  print(int(w_out)) # output width count
#  print(int(adds))  # number of additions performed
#  print(int(muls))  # number of multiplications performed
#  print(int(divs))  # number of divisions performed
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# initialize script arguments
c_in = 0.0
h_in = 0.0
w_in = 0.0
h_pool = 0.0 
w_pool = 0.0 
s = 0.0 
p = 0.0

# parse script arguments
if len(sys.argv)==8:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    h_pool = float(sys.argv[4]) 
    w_pool = float(sys.argv[5]) 
    s = float(sys.argv[6]) 
    p = float(sys.argv[7])
    
else:
   print(\
    'Usage: '\
    'pool_ops.py c_in h_in w_in h_pool w_pool s p'\
   )
   exit()

# write script below this line

c_out = c_in
h_out = (1/s) * (h_in + 2*p - h_pool) + 1
w_out = (1/s) * (w_in + 2*p - w_pool) + 1
adds = h_out*w_out*c_in*(h_pool*w_pool-1)
divs = h_out*w_out*c_in

#Due to Pool Layer
muls = 0

#output
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed