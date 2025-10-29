import house as h

def test_house_rooms():
       print()
       # Room object is managed by house object
       house = h.House(["Living Room", "Kitchen", "Bedroom"])
       house.show_house_layout()
       