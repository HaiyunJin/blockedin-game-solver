
class state:
    ''' object: state '''
    def __init__(self,parent,mode):
        ''' create a state with mode'''
        self.parent=parent
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
            # judge and move
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
            # judge and move
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
        ''' add to dead library'''
        drop=0
        for item in self.lib:
            if instance.mode == item.mode:
                drop=1
        if drop == 0 :
            self.lib.append(instance)

    def DeleteItem(self,mode):
        ''' Delete the instance that match the given mode'''
        for item in self.lib:
            if item.mode ==  mode:
                self.lib.pop(self.lib.index(item))

    def Inlib(self,mode):
        ''' Check if the instance is in the library. '''
        for item in self.lib:
            if mode == item.mode:
                return True
        return False

    def print_lib(self):
        for item in self.lib:
            print item.mode


def parent_mode_of(mode):
    ''' Find the parent mode of a certain mode'''
    for item in all_lib.lib[:]:
        if item.mode == mode:
            return item.parent


def search(instance,dead_lib,search_lib,all_lib):

 #   print "Search is Called"

    # add the current state to dead_lib
    print instance
    search_lib.AddItem(instance)
    all_lib.AddItem(instance)
    #print len(dead_lib.lib)

#    print 'dead_lib' , dead_lib.lib
    if (instance.mode[16] == 1) and (instance.mode[17] == 1) :
        print "Found"
        return instance.mode

    # move block if can, and compare
    allblock=1
    for block in instance.blocks:
        #print 'Now, processing block', block
        thisblockold=1
        for direction in [1,-1]:
            #print 'Now, direction', direction
            newmode=instance.move(block,direction)

#            print "Newmode", newmode, newmode[11]
#            print 'My  lib'
#            search_lib.print_lib()
            if dead_lib.Inlib(newmode):         # if in dead lib, delete
                # if in dead_lib, remove it from search_lib
                #if search_lib.Inlib(newmode):   # in if search lib, then stop, leave it.
                #    search_lib.DeleteItem(newmode)
                    thisblockold=1
 #                   print 'here1'
            else:           # or try search search lib
                if search_lib.Inlib(newmode):   # in if search lib, then stop, leave it.
                    thisblockold=1
 #                   print 'here2'
                    #result=search(new,dead_lib,search_lib,all_lib)
                    #dead_lib.AddItem(new)
                else:               # or add it to search lib and search
#                    print 'newmodeindepth', newmode
                    new=state(instance,newmode)
                    all_lib.AddItem(new)
                    search_lib.AddItem(new)
                    thisblockold=0
                    #print 'thisblockold',thisblockold
                    print 'here new'
                    #result=search(new,dead_lib,search_lib,all_lib)
            #print 'thisblockold',thisblockold
        allblock*=thisblockold
#        print 'allblock' , allblock
    # if no new mode, then, put into dead_lib
    if allblock == 1:
    #    print 'allblock' , allblock
        dead_lib.AddItem(instance)
        if search_lib.Inlib(instance.mode):   # in if search lib, then stop, leave it.
            search_lib.DeleteItem(instance.mode)
#            print 'Delete item in searchlib'

#        print 'modes in dead_lib'
#        dead_lib.print_lib()

    #print 'allblock' , allblock
#    print 'modes in search_lib'
    #search_lib.print_lib()
    #result=search(search_lib.lib[-1],dead_lib,search_lib,all_lib)
    result=False

    return result




initial=[ 2,  0,  5,  5,  9,  9,
         2,  0,  0,  6, 11, 11,
         1,  1,  4,  6, 10,  0,
         3,  3,  4,  8, 10, 12,
         7,  7,  4,  8, 10, 12,
         0,  0,  0, 13, 13, 13]
initial= [0, 0, 0, 4, 0, 0,
3, 3, 3, 4, 0, 0,
1, 1, 2, 4, 0, 6,
0, 0, 2, 7, 7, 6,
5, 5, 5, 0, 0, 8,
0, 0, 0, 0, 0, 8]





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
#        search_lib.print_lib()
#    if i == 10 :
#        print 'len of search lib', len(search_lib.lib)
#        print '  len of dead lib', len(dead_lib.lib)
#        print '   len of all lib', len(all_lib.lib)
#        search_lib.print_lib()
#        print 'exit'
#        exit()
#




print i

# find the route
mode=resultmode
print 'mode',mode
while mode != None:
    print 'modein',mode
    mode=parent_mode_of(mode)
    print mode


