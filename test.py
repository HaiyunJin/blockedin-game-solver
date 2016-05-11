class a:
    def __init__(self,b):
        self.data=b

    def out(self):
        self.dd=self.data
        if self.dd == 1:
            return self.dd

        print 'no'
        return 'nothing'



aa=[]
aa.append(a(1))
aa.append(a(2))
aa.append(a(3))
aa.append(a(4))

bb=[]
bb.append(a(1))
bb.append(a(2))
bb.append(a(3))
bb.append(a(5))

#print aa
for x in aa:
    print x.data

print '===='

for i in aa[:]:
    for j in bb[:]:
        if i.data == j.data:
            aa.pop(aa.index(i))

for x in aa:
    print x.data


