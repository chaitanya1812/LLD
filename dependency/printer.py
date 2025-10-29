class Document:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content

class Printer:
    def print(self, document):  # dependency: Document
        print("Printing:", document.get_content())