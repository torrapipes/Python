from regularitem import RegularItem

class AgedBrie(RegularItem):

    

    
    def update_quality(self):

        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()

    


if __name__ == '__main__':

    item = AgedBrie("Aged Brie", 2, 0)
    print(item)

    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

    # test update_quality incorret input
    item = AgedBrie("Aged Brie", 2, 100)
    for dia in range(1, 10):
        item.update_quality()
        print(item)