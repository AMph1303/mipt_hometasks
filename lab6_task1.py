class Dict(dict):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)

    def __add__(self, other):
        self.update(other)
        return self

    def add(self, y):
        self+y
        return self  
            
    @classmethod
    def from_default(cls, self): 
        res = Dict()   
        for key, value in self.items(): 
            res + {key : value}
        self = res
        return self        

def test():
    d = Dict()
    print(d)

    a = Dict(a1=20, b1=10)
    b = dict(x=1, y=2, z=3)
    c = Dict(t=1, w=2, u=5)

    print(a+b)
    print(c.add(b))
    print(d + {'d':2})
    print(type(Dict.from_default(b)))


    print(a["a1"])
    a["a3"] = 5
    print(a)
    print(len(a))
    
    
if __name__ == "__main__":
    test()  
