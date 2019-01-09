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
        self.setSell_in()

    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value > 0:
            self.quality += value 
        else: 
            self.quality = 0
    
    def getName(self):
        return self.name

    def getSell_in(self):
        return self.sell_in
    
    def getQuality(self):
        return self.quality


if __name__ == '__main__':


    # CREATED AN OBJECT
    duck = RegularItem("duck", 0, 4)
    duck.update_quality()
    
    # TEST CASES
    assert duck.getSell_in() == -1
    assert duck.getQuality() == 2

    # CREATED AN OBJECT
    dog = RegularItem("dog", 100, 1)

    # TEST CASES
    assert dog.getName() == "dog"
    assert dog.getSell_in() == 100
    assert dog.getQuality() == 1
    