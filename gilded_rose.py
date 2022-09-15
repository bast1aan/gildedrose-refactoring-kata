class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        new_items = []
        for item in self.items:
            new_item = Item(item.name, item.sell_in, item.quality)
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        new_item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    new_item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if new_item.quality < 50:
                            if item.sell_in < 11:
                                new_item.quality = new_item.quality + 1
                            if item.sell_in < 6:
                                new_item.quality = new_item.quality + 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                new_item.sell_in = item.sell_in - 1
            if new_item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if new_item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                new_item.quality = new_item.quality - 1
                    else:
                        new_item.quality = 0
                else:
                    if new_item.quality < 50:
                        new_item.quality = new_item.quality + 1
            new_items.append(new_item)
        self.items = new_items

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
