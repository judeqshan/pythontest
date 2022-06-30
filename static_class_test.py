class parent:
    parent_var = "parent"
    def __init__(self):
        self.parent_local = "parent local"

    def f1_p(self):
        print(self.child_var)

class child(parent):
    child_var = "child"
    def __init__(self):
        super(child, self).__init__()
        child_local = "child local"

    def f1_c(self):
        pass

def main():
   parent.parent_var = "new added parent"
   child.child_var = "child var"
   p = parent()
   p.f1_p()
#    ch = child()
#    print(ch.parent_var)
#    print(ch.f1_p())
#    print(ch.parent_local)
#    ch.f1_p()
    
    


if __name__ == '__main__':
    main()