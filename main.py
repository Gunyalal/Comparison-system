from tabulate import tabulate

m=6
n=5

class vTable:
  def __init__(self,m,n):
    self.m=m
    self.n=n
    compTable = [[0 for i in range(n)] for j in range(m)]
    mst = 0 #m step
    nst = 0 #n step
    for i in range(0,m*n):
      compTable[mst][nst] = i
      print(mst,nst, i)
      mst+=1
      nst+=1
      if mst==m:
        mst=0
      if nst==n:
        nst=0
    header = ["n\m"]
    for i in range(0,n):
      header.append(i)
    for i in range(m):
      compTable[i].insert(0,i)
    self.compTable = compTable
    self.header = header

VT = vTable(n,m)

print(tabulate(VT.compTable, headers = VT.header, tablefmt="grid"))