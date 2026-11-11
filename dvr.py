INF = 999
n = int(input("enter no. of router:"))
cost = []
for i in range(n):
  row=  list(map(int,input(f"ROW {i}:").split()))
  cost.append(row)

dist=[]
for row in cost:
  dist.append(row.copy())
for iteration in range(1,n):
  new_dist=[]
  for i in range(n):
    row=[]
    for j in range(n):
      row.append(dist[i][j])
    new_dist.append(row)
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if cost[i][k]!=INF and cost[k][j]!=INF:
          new_cost =cost[i][k]+dist[k][j]
          if new_cost<new_dist[i][j]:
            new_dist[i][j]=new_cost
  dist =new_dist
print(dist)