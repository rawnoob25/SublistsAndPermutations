def gen_2partition_sublist(L):
    """
    This function generates disjoint pairs of sublists of L. Each such pair is a tuple. The
    function returns the list of all such tuples. The output
    returned by this function can be used to answer the question: "How many different
    pairs of knapsacks can be constructed from the function L such that
    any element in the list may be absent from both knapsacks, or may be present
    in either of the knapsacks (but never both).
    """
    n=len(L)
    out=[]
    for i in range(3**n):
        knap1,knap2=[],[]
        psn=0
        k=i
        while k>0:
            #determine value of psn-th digit of base-3 representation
            #of k; if it's 1, add L[psn] to knap1; otherwise if it (psn-th digit) is 2, add
            #L[psn] to knap2.
            if k%3==1:
                knap1.append(L[psn])
            elif k%3==2:
                knap2.append(L[psn])
            else:
                pass
            k//=3
            psn+=1
        out.append((knap1,knap2))
    return out

def twoPartitionSublist_generator(L):
    """This function returns a generator that yields disjoint pairs of sublists of L. Each such pair
       is a tuple. Each tuple yielded by the generator is one possible value-set for a pair of
       knapsacks- each member of which contains items from list L; no item of L is present in both knapsacks.
    """
    n=len(L)
    for i in range(3**n):
        knap1,knap2=[],[]
        psn=0
        k=i
        while k>0:
            #determine value of psn-th digit of base-3 representation
            #of k; if it's 1, add L[psn] to knap1; otherwise if it (psn-th digit) is 2, add
            #L[psn] to knap2.
            if k%3==1:
                knap1.append(L[psn])
            elif k%3==2:
                knap2.append(L[psn])
            else:
                pass
            k//=3
            psn+=1
        yield((knap1,knap2))

def gen_sublists(L):
    """
    This function generates sublists of L. The output returned by this function
    can be used to answer the question: "What are all of the possible
    knapsacks of items that can be constructed using elements in this list such
    that a given element either be present in the knapsack, or fail to be present
    in the knapsack?"

    >>> gen_sublists(list("foo"))
    [[], ['f'], ['o'], ['f', 'o'], ['o'], ['f', 'o'], ['o', 'o'], ['f', 'o', 'o']]
    """
    def gen_bit_strings(n):
        if n==0:
            return [""]
        L_n_1 = gen_bit_strings(n-1)
        out=[]
        for e in L_n_1:
            out.append("0"+e)
            out.append("1"+e)
        return out
    bitStrings = gen_bit_strings(len(L))
    sublists=[]
    for s in bitStrings:
        sublists.append([L[i] for i in range(len(s)) if int(s[i])]) # this is
        #equivalent to sublists.append(L[i] for i in range(len(s)) if int(s[i])==0)
    return sublists

def sublist_generator(L):
    """
    Returns a generator that can be used to obtain sublists of L
    """
    def gen_bit_strings(n):
        if n==0:
            return [""]
        L_n_1 = gen_bit_strings(n-1)
        out=[]
        for e in L_n_1:
            out.append("0"+e)
            out.append("1"+e)
        return out
    bitStrings = gen_bit_strings(len(L))
    for s in bitStrings:
        yield([L[i] for i in range(len(s)) if int(s[i])])
    
    

def second_gen_sublists(L):
    """
    This function uses bitshifting to generate sublists
    """
    n=len(L)
    allSublists=[]
    for i in range(2**n):
        sublist=[]
        k=i
        psn=0
        while k>0:
            if k%2==1:
                sublist.append(L[psn])
            k//=2
            psn+=1
        allSublists.append(sublist)
    return allSublists

def second_sublist_generator(L):
    """This function also returns a generator that can be used to yield elements
       of L; however, the computation to obtain each sublist uses bitshifting
       rather than using a bitstring to index into list L
    """
    n=len(L)    
    for i in range(2**n):
        sublist=[]
        k=i
        psn=0
        while k>0:
            if k%2==1:
                sublist.append(L[psn])
            k//=2
            psn+=1
        yield sublist
        
def sameElements(L1,L2):
    """
    parameters: lists L1 and L2
    precondition: L1 and L2 are lists holding elements
    that are the same type as other elements in the list
    and are also the same type as one another
    """
    if len(L1)!=len(L2):
        return False
    for e in L1:
        if e not in L2:
            return False
    for e in L2:
        if e not in L1:
            return False
    return True

assert sameElements(range(1,7),range(6,0,-1))
assert not sameElements([1,2],[1,3])
assert not sameElements([1,2],[1,2,3])
assert not sameElements([1,2,3],[1,2])

def endFn(val):
    return val>=10

def generator2(f):
    """
    precondition: f is a boolean returning function that takes an int as a parameter
    """
    i=0
    while i<20:
        if f(i):
            return
        yield(i)
        i+=1



testLists=[list("foo"),list("23"),list(""),list("1"),list("lote"),list("loose"),
           list("ooo")]
for L in testLists:
    L1=gen_sublists(L)
    L2=second_gen_sublists(L)
    print(L1, end="\n\n")
    print(L2)
    assert sameElements(L1,L2)
    print("------------------------")

print("TESTING gen_2partition_sublist")

testLists=[list("of"), list("foo")]
for L in testLists:
    twoSublistPartitions=gen_2partition_sublist(L)
    assert len(twoSublistPartitions)==3**len(L)
    print(L)
    print(twoSublistPartitions, end="\n\n")
    print("-------------------------")


print("TESTING generator2")
for x in generator2(endFn):
    print(x)

print("TESTING sublist_generator")
L = list("foo")
for e in gen_sublists(L):
    print(e, end=" ")
print("")

print("TESTING second_sublist_generator")
L = list("foo")
for e in second_sublist_generator(L):
    print(e, end=" ")
print("")


print("TESTING twoPartitionSublist_generator")
L = list("foo")
twoSublistPartitions=gen_2partition_sublist(L)
i=0
for e in twoPartitionSublist_generator(L):
    assert e==twoSublistPartitions[i]
    i+=1
