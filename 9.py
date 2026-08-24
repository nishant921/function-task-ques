# write a python function that accepts a list of 2D co-ordinate and the query point and then find the co-ordinate which is closet in terms of distance from the query point
def short_dis(point,query):
        temp=point
        l=[]
        for i in point:
            d=(((i[0]-query[0])**2) + ((i[1]-query[1])**2))**0.5
            l.append(d)
        return point[sorted(list(enumerate(l)), key= lambda x:x[1])[0][0]]
            
        
        
point=[(1,4),(2,-2),(3,3)]
query=(0,0)
print(short_dis(point,query))


