class Item():


    def __init__(self, name, sell_in, quality):

        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self, name, sell_in, quality):

        return '%s, %s, %s' % (self.getName(), self.getSell_in, self.getQuality)

    def getName(self):

        return self.name

    def getSell_in(self):

        return self.sell_in
    
    def getQuality(self):

        return self.quality


if __name__ == '__main__':

    # CREATED OBJECT
    Duck = Item("Duck", 100, 1)

    # TEST CASES
    assert duck.getName() == "Duck"
    assert duck.getSell_in() == 100
    assert duck.getQuality() == 1