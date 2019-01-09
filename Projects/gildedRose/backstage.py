from regularItem import RegularItem

class backstage(RegularItem):

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()


if __name__ == '__main__':

    # CREATED AN OBJECT
    Duck = backstage("Duck", 9, 3)
    Duck.update_quality()

    # TEST CASES
    assert Duck.getQuality() == 1
    assert Duck.getSell_in() == 8

