# A disjoint set forest is a data structure that has two operations:
# ``find`` and ``union``. ``find(x)`` finds the set that an element ``x``
# belongs to, so that one can ask questions like "Are elements a and b in
# the same set?". ``union(x,y)`` joins the two sets that ``x`` and ``y``
# belong to. This data structure was learned in CS 170 and is crucial for
# use in finding the minimum spanning tree of a graph (Kruskal's
# algorithm).
#
# The data structure is extremely efficient, because with the use of path
# compression, an amortized time of nlog*n time can be achieved on
# consecutive finds.
#
# The (relatively) inefficient versions of the ``find`` function are
# commented out but left for clarity.

class DisjointSetForest:
    def __init__(self):
        ''' Makes a disjoint set forest (ie. a set of sets). '''
        self.parent = {}
        self.rank = {}
        self.roots = set()  # definitive list of all roots (ie. all sets)
        self.size = {}  # size of set rooted at sx, parent of x

    def insert(self, x):
        '''
        Dumb insert that just places the element in the set forest in its own
        set. This set can be merged with other sets later on.
        '''
        self.parent[x] = x
        self.rank[x] = 0
        self.size[x] = 1
        self.roots.add(x)

    def find(self, x):
        '''
        Finds which root node (ie. which set) this data structure belongs
        to. Utilizes path compression so that the amortized runtime of this
        operation is barely over O(1) time.
        '''
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        '''
        Unions the sets that ``x`` and ``y`` belong to. In addition, since
        I added the additional ``size`` and ``roots`` tracker from the
        standard data structure, therefore correspondingly updates these as
        well on each union. The size of the set with lower rank is added to
        the size of the set with higher rank, and the root of the set with
        lower rank is removed as a definitive root node in the structure.
        '''
        sx = self.find(x)
        sy = self.find(y)
        if sx == sy: return
        if self.rank[sx] > self.rank[sy]:
            self.parent[sy] = sx
            self.size[sx] += self.size[sy]
            del self.size[sy]  # only makes sense for root to have size
            self.roots.remove(sy)
        elif self.rank[sx] < self.rank[sy]:
            self.parent[sx] = sy
            self.size[sy] += self.size[sx]
            del self.size[sx]
            self.roots.remove(sx)
        else:  # equal rank
            self.parent[sx] = sy
            self.size[sy] += self.size[sx]
            del self.size[sx]
            self.roots.remove(sx)
            self.rank[sy] = self.rank[sy] + 1

def neighbors(grid, i, j):
    '''
    Enumerates the neighbors of a position (i, j), given the constraints of
    ``grid``.
    '''
    for a in xrange(-1, 2):
        if i + a < 0 or i + a >= len(grid):
            continue
        for b in xrange(-1, 2):
            if j + b < 0 or j + b >= len(grid) or a == b == 0:
                continue
            yield (i + a, j + b, grid[i + a][j + b])

S = int(raw_input())
D = DisjointSetForest()
grid = []

for i in xrange(S):
    row = map(int, raw_input().split())
    grid.append(row)
    for j, el in enumerate(row):
        D.insert( (i, j, el) )

# union each cell with its min neighbor (if the current node isn't a sink)
for i, row in enumerate(grid):
    for j, el in enumerate(row):
        try:
            x, y, a = min( neighbors(grid, i, j), key=lambda (x, y, a): a )
            if a < el:
                D.union((i, j, el) , (x, y, a))
        except ValueError:
            pass  # edge case: no neighbors

# enumerate the sets and size
print ' '.join( str(x) for x in reversed( sorted( D.size[x] for x in D.roots ) ) )
