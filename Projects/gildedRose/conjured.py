from regularItem import RegularItem

class Conjured(RegularItem):


    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)


if __name__ == '__main__':

    # CREATED OBJECT
    conjured = Conjured("Conjured", 100, 20)
    conjuredMana = Conjured("Conjured Maná", -2, 20)
    conjured.update_quality()
    conjuredMana.update_quality()

    # TEST CASES
    assert conjured.getQuality() == 19
    assert conjuredMana.getQuality() == 18