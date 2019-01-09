from item import Item
from updatable import Updatable

class RegularItem(Item, Updatable):


    def setSell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.getSell_in() > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in ()

    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value > 0:
            self.quality += value 
        else: 
            self.quality = 0


if __name__ == '__main__':


    # CREATED AN OBJECT
    Duck = RegularItem("Duck", 0, 4)
    Duck.update_quality()
    
    # TEST CASES
    assert Duck.getSell_in() == -1
    assert Duck.getQuality() == 2
    