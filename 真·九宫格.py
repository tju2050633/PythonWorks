import itertools
import numpy as np
name=[x for x in range(1,10)]
sequence_3nums=[p for p in itertools.permutations(name,3)  if sum(p)==15]
for row1_1,row1_2,row1_3 in sequence_3nums:
    for row2_1,row2_2,row2_3 in sequence_3nums:
        for row3_1,row3_2,row3_3 in sequence_3nums:
            if row1_1+row1_2+row1_3==15\
               and row2_1+row2_2+row2_3==15\
               and row3_1+row3_2+row3_3==15\
               and row1_1+row2_1+row3_1==15\
               and row1_2+row2_2+row3_2==15\
               and row1_3+row2_3+row3_3==15\
               and row1_1+row2_2+row3_3==15\
               and row1_3+row2_2+row3_1==15:
                if len(set([row1_1,row1_2,row1_3])&set([row2_1,row2_2,row2_3]))==0:
                    nums=np.array([[row1_1,row1_2,row1_3],[row2_1,row2_2,row2_3],[row3_1,row3_2,row3_3]])
                    print(nums)
