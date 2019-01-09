from item import Item
from updatable import Updatable

class RegularItem(Item, Updatable):


    def setSell_in(self):
        return self.sell_in - 1

    def update_quality(self):
        if self.sell_in > 0:
            return self.quality - 1
        else:
            return self.quality - 2


if __name__ == '__main__':

    # CREATED AN OBJECT
    Duck = RegularItem(0, 4)

    # TEST CASES
    assert Duck.setSell_in() == -1
    assert Duck.update_quality() == -2