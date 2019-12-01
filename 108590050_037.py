"""
037

給定兩個字串，A為父字串，B為子字串，
請在A中找出最短字串C，
且B必須為C的子集。

範例輸入說明:

M = CDEBATC
S = ABC

範例輸出說明:
BATC

因CDE{BATC}中，為最短且都有ABC的情況，
所以輸出為BATC，雖然CDEBA也滿足，
但它不是最短的。

sample input:

CDEBATC
ABC

sample output:

BATC

-----------------------------------------
sample input2:

ABCBCAABABAC
ACCAB

sample output2:

CBCAA

note:題目不會有找不到或是有兩個同長度且滿足需求的情況!!!
"""

M=input()
S=input()
M_set=set(M)
S_set=set(S)
ref_dict={i:S.count(i)for i in M_set}
for i in range(len(S),len(M)+1):
    for j in range(len(M)-i+1):
        tmp_set=set(M[j:j+i])
        if S_set <= tmp_set:
            tmp_dict={k:M[j:j+i].count(k)for k in tmp_set}
            for k in S_set:
                if(tmp_dict[k]!=ref_dict[k]):break
            else:
                print(M[j:j+i])
                break
    else:continue
    break
