d1 = {'A':'1'}
d2 = {'A':'1', 'B':'2'}
d3 = {'A':'1', 'B':'2','C':'3'}

common = set(d3.keys()).union(set(d1.keys()).union(set(d2.keys())))
print(common)

