from regularItem import RegularItem

class AgedBrie(RegularItem):


    def update_quality(self):

        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()


if __name__ == '__main__':

    Duck = AgedBrie("Aged Brie", 2, 0)
    Duck.update_quality()

    assert Duck.getQuality() == 1
    