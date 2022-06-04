data = [set(('i1','i2','i4')),set(('i2','i4')),set(('i1','i2','i5')),set(('i2','i3'))]
id_dict = {'A':0,'B':1,'C':2,'D':3}
W=[]
u=0
for i in data:
    W.append([])
    for j in data:
        W[u].append(len(i.intersection(j))/len(i.union(j)))   #Jaccarrd相似度
    u+=1 
def Recommend(data=data,id_dict=id_dict,user_id='A',W=W,K=2):  
    int_id=id_dict[user_id]
    w_tmp=W[int_id]
    w=dict()
    for i in range(len(w_tmp)):
        w[i]=w_tmp[i]
    g=set()
    ID=[]
    rank=dict()
    for j,wj in sorted(w.items(),key=lambda d: d[1],reverse=True)[0:K+1]:   
        if(j!=int_id):
            g=g.union(data[j])   
            ID.append(j)
    g=list(g.difference(data[int_id]))
    p_rank=dict()
    for i in g:
        p_rank[i]=0
        for j in ID:
            p_rank[i]+=(len(data[int_id].intersection(data[j]))/len(data[int_id].union(data[j])))*( i in data[int_id].union(data[j]))
    return p_rank
p_rank=Recommend()   
print("A的相似度")         
print(p_rank)