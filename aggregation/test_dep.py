import department as d

def test_department():
    print("")
    # create 2 professor objects independently
    p1 = d.Professor("P1")
    p2 = d.Professor("P2")
    p3 = d.Professor("P3")

    # add profs to departments
    dep1 = d.Department("CS", [p1, p2])
    dep1.print_professors()

    dep2 = d.Department("ECE", [p1]) # prof can be part of multiple deps
    dep2.print_professors()
    
    # can deal with p3 independtly even when p3 not part of any department
    print(p3.get_name())