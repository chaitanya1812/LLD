import printer as p
def test_printer():
    print()
    doc = p.Document("Hello")
    printer = p.Printer()
    printer.print(doc)