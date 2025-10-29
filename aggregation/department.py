class Department:
    def __init__(self, name, professors):
        self.name = name
        self.professors = professors

    def print_professors(self):
        print(f"Professors in {self.name} Department:")
        for professor in self.professors:
            print(f"- {professor.get_name()}")

class Professor:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    

