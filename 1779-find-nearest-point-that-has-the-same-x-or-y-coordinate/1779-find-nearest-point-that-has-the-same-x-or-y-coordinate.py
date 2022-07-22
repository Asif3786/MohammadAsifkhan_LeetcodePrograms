class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mi=-1
        dist=float("inf")
        def validate(x,y,p):
            return x==p[0] or y==p[1]  
        def distance(x,y,p):
            return abs(x-p[0])+abs(y-p[1])
        for p in points:
            if validate(x,y,p):
                d=distance(x,y,p)
                if d<dist:
                    mi=points.index(p)
                    dist=d
        return mi            
                
                        
            
       
        
        
       
                    
                    
        