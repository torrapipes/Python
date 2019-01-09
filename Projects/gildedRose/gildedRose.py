from backstage import Backstage
from aged_brie import AgedBrie
from sulfuras import Sulfuras

class GildedRose():


    def __init__(self, stock):
        self.stock = stock
    
    def getStock(self):
        return self.stock

    def updateStock(self, stock):
        for item in self.stock:
            item.update_quality()


if __name__ == '__main__':

    # CREATED STOCK
    stock = [AgedBrie("agedBrie", 100, 20), Backstage("backstage", 15, 10), Sulfuras("sulfuras", 10, 80)]
    store = GildedRose(stock)
    store.updateStock(stock)

    # TEST CASES
    assert 80 == store.getStock()[2].getQuality()
    assert 21 == store.getStock()[0].getQuality()
    assert 11 == store.getStock()[1].getQuality()
