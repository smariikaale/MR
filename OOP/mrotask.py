#finf mro of F:
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    def greet(self):
        print("Hello from D")

class E(C, B):
    def greet(self):
        print("Hello from E")

class F(D, E):
    def greet(self):
        print("Hello from F")
        
print(F.mro())
#MRO(A)=[A,object]
#MRO(B)=B+merge([A,object],[A])
#      =[B,A,object]
#MRO(C)=[C]+merge([A,object],[A])
#       =[C,A,object]
#MRO(D)=[D]+merge(MRO(B),MRO(C),[B,C])
#       =[D]+merge([B, A, object], [C, A, object], [B, C])//since B is in head
#       =[D,B]+merge([A,object],[C,A,object],[C])//since C is not in tail
#       =[D,B,C]+merge([A,object],[A,object])
#       =[D,B,C,A,object]
#MRO(E)=[E]+merge(MRO(C),MRO(B),[C,B])
#      =[E]+merge([C,A,object],[B,A,object],[C,B])//since B is not in tail of any other lists
#      =[E,B]+merge([C,A,object],[A,object],[C])
#      =[E,B,C]+merge([A,object],[A,object],[])
#      =[E,B,C,A,object]
#MRO(F)=[F]+merge(MRO(D),MRO(E),[D,E])
#      =[F]+merge([D,B,C,A,object],[E,B,C,A,object],[D,E])//D is not in tail of any list so taking D out
#      =[F,D]+merge([B,C,A,object],[E,B,C,A,object],[E])
#      =[F,D,E]+merge([B,C,A,object],[B,C,A,object],[]
#      =[F,D,E,B]+merge([C,A,object],[C,A,object])
#      =[F,D,E,B,C]+merge([A,object],[A,object])
#      =[F,D,E,B,C,A,object]