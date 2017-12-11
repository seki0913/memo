def scope_test():
    def do_local():
        spam = "local spam"
    #def do_nonlocal():
    #    nonlocal spam
    #    spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "grobal spam"
    spam = "test spam"

    # do_nonlocal()
    # print("After nonlocal assignment:", spam)
    do_global()
    print("After grobal assignment:", spam)
    do_local()
    print("After local assignment:", spam)
    
scope_test()
print("In grobal Scope:", spam)