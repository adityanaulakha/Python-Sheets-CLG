# 13. How can you generate a list of cumulative sums of elements in the provided list arr,
# utilizing Python's itertools.accumulate() function along with a lambda function?

import itertools as i
arr = [1,2,3,4,5]
print(list(i.accumulate(arr,lambda x,y: x+y)))