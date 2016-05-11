
# 2.1   modify the inlib function, return postion  or False


class state:
    ''' object: state '''
    def __init__(self,parent,mode):
        ''' create a state with mode'''
        self.parent=parent
        if parent == None:
            self.generation=0
        else:
            self.generation=parent.generation+1
        self.mode=mode
        self.blocks=[]
        self.nblocks=0
        for block in self.mode:
            if block not in self.blocks:
                if block != 0 :
                    self.blocks.append(block)
                    self.nblocks+=1
        # remove blocks name 0

    def move(self,block,direction):
        ''' move a block.
        Direction, up 1; down -1; left -1; right 1
        '''
        # block occupies at
        pos=[i for i, j in enumerate(self.mode) if j == block ]
#        print 'pos', pos
        new=self.mode[:]

        # determine the block type, vertical or horizon
        if block%2 == 0:
            # can move only vertically
            if direction == 1:  # move up
                top=pos[0]-6   # 6 is the dimension
                if top >= 0 and new[top] == 0 :
                    new[top] = block
                    new[pos[-1]] = 0
#                    print 'move up'
            else:               # move down
                bottom=pos[-1]+6
                if bottom <= 35 and new[bottom] == 0:
                    new[bottom]=block
                    new[pos[0]] = 0
#                    print 'move down'
        else:
            # can only move horizonly
            if direction == 1:  # move up
                left=pos[0]-1   # 6 is the dimension
                if left >= 0 and new[left] == 0 and pos[0]%6 != 0 :
                    new[left] = block
                    new[pos[-1]] = 0
#                    print 'move left'
            else:               # move down
                right=pos[-1]+1
                if right <= 35 and new[right] == 0 and right%6 !=0:
                    new[right]=block
                    new[pos[0]] = 0
#                    print 'move right'
        return new

class library():
    ''' library to store instance'''
    def __init__(self):
        self.lib=[]

    def AddItem(self,instance):
        ''' add to dead library, the instance is new'''
        self.lib.append(instance)
    #   drop=0
    #   for item in self.lib:
    #       if instance.mode == item.mode:
    #           drop=1
    #   if drop == 0 :
    #       self.lib.append(instance)

    def DeleteItem(self,mode):
        ''' Delete the instance that match the given mode'''
    #   self.lib.pop(self.lib.index(item))
        for item in self.lib:
            if item.mode ==  mode:
                self.lib.pop(self.lib.index(item))

    def update(self,instance):
        ''' if the mode is in lib, update to the smaller generation one'''
        for item in self.lib:
            if item.mode == instance.mode:
                if instance.generation < item.generation:
                    self.lib.pop(self.lib.index(item))
                    self.lib.append(instance)

    def Inlib(self,mode):
        ''' Check if the instance is in the library. '''
        for item in self.lib:
            if mode == item.mode:
                return self.lib.index(item)
        return None

    def print_lib(self):
        for item in self.lib:
            print item.mode



def parent_of(mode):
    ''' Find the oldest parent object of a certain mode'''
    first=True
    for item in all_lib.lib[:]:
        if item.mode == mode:
            if first:
                candidate=item
                first=False
            elif item.generation < candidate.generation:
                candidate=item

    return candidate.parent
#    return None


def search(instance,dead_lib,search_lib,all_lib):

    if dead_lib.Inlib(instance.mode) != None:   # in if search lib, then stop, leave it.
        dead_lib.AddItem(instance)
        search_lib.DeleteItem(instance.mode)
        if all_lib.Inlib(instance.mode) != None:  # if the dead in in all lib, delete it to save time
            all_lib.DeleteItem(instance.mode)
        return False

 #   print "Search is Called"

    all_lib.AddItem(instance)
    #print len(dead_lib.lib)

    if (instance.mode[15] == 1) and (instance.mode[16] == 1) and (instance.mode[17] == 0) :
        print "Found"
        return instance.mode

    # move block if can, and compare
    allblock=1
    for block in instance.blocks:
#        thisblockold=1
        for direction in [1,-1]:
            newmode=instance.move(block,direction)
            if dead_lib.Inlib(newmode) != None:   # in if search lib, then stop, leave it.
                pass
            else:
                new=state(instance,newmode)
                if search_lib.Inlib(newmode) != None:
                    # compare generation, if smaller, replace
                    search_lib.update(new)
                else:
                    search_lib.AddItem(new)
#                    thisblockold=0
                    allblock=0

    # if no new mode, then, put into dead_lib
    if allblock == 1:
    #    print 'allblock' , allblock
        dead_lib.AddItem(instance)
        search_lib.DeleteItem(instance.mode)  # it is dead

    return False








#level 7x ish
initial=[
 2, 0, 5, 5, 9, 9,
 2, 0, 0, 6,11,11,
 1, 1, 4, 6,10, 0,
 3, 3, 4, 8,10,12,
 7, 7, 4, 8,10,12,
 0, 0, 0,13,13,13]



# level 94
initial=[
 2, 4, 7, 7,10,12,
 2, 4, 0, 8,10,12,
 2, 1, 1, 8, 0,12,
 0, 3, 3, 0, 9, 9,
 0, 0, 6, 0,11,11,
 5, 5, 6,13,13, 0]

# level easy
initial= [
 0, 0, 0, 4, 0, 0,
 3, 3, 3, 4, 0, 0,
 1, 1, 2, 4, 0, 6,
 0, 0, 2, 7, 7, 6,
 5, 5, 5, 0, 0, 8,
 0, 0, 0, 0, 0, 8]



#level 1
initial=[
 0, 0, 2, 0, 0, 0,
 0, 0, 2, 0, 0, 0,
 1, 1, 2, 4, 0, 6,
 0, 0, 0, 4, 0, 6,
 0, 0, 0, 4, 0, 0,
 0, 3, 3, 5, 5, 0]


new=state(None,initial)

dead_lib=library()
search_lib=library()
all_lib=library()
#search_lib.Add(new)

#print new , dead_lib , search_lib

#def search(self,instance,dead_lib,search_lib):
resultmode=search(new, dead_lib, search_lib, all_lib)

print 'first resultmode', resultmode

i=0
#while len(search_lib.lib) != 0:
resultmode = False
while resultmode == False:
    resultmode=search(search_lib.lib[-1], dead_lib, search_lib, all_lib)
    i+=1
    for x in search_lib.lib[:]:
        for dead in dead_lib.lib[:]:
            if x.mode == dead.mode :
                search_lib.DeleteItem(x.mode)

    if i % 1000 == 0 :
        print i
        print 'len of search lib', len(search_lib.lib)
        print '  len of dead lib', len(dead_lib.lib)
        print '   len of all lib', len(all_lib.lib)
        print '======================='

print i
print 'len of search lib', len(search_lib.lib)
print '  len of dead lib', len(dead_lib.lib)
print '   len of all lib', len(all_lib.lib)

solut=[]
# find the route
mode=resultmode

solut.append(mode)

while mode != None:
    temp=parent_of(mode)
    if temp != None:
        mode=temp.mode
        solut.append(mode)
        #print mode
    else:
        mode=None

solut.reverse()

print "One doable route:"
for mode in solut:
    print '%3d%3d%3d%3d%3d%3d' % (mode[0], mode[1], mode[2], mode[3], mode[4], mode[5] )
    print '%3d%3d%3d%3d%3d%3d' % (mode[6], mode[7], mode[8], mode[9], mode[10],mode[11])
    print '%3d%3d%3d%3d%3d%3d' % (mode[12],mode[13],mode[14],mode[15],mode[16],mode[17])
    print '%3d%3d%3d%3d%3d%3d' % (mode[18],mode[19],mode[20],mode[21],mode[22],mode[23])
    print '%3d%3d%3d%3d%3d%3d' % (mode[24],mode[25],mode[26],mode[27],mode[28],mode[29])
    print '%3d%3d%3d%3d%3d%3d' % (mode[30],mode[31],mode[32],mode[33],mode[34],mode[35])
    print '====================='

print "Route printed"
print 'Search iterations:', len(solut)


