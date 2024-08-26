# 12. Find the maximum element in a list using lambda and reduce () function?

import functools as f
arr = [1,2,3,4,5]
print(f.reduce(lambda x,y:x if x>y else y,arr))