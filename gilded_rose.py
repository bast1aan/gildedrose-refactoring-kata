from __future__ import annotations

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def handle_aged_brie(self, item) -> Item:
        quality = item.quality
        sell_in = item.sell_in
        if item.quality < 50:
            quality += 1
        sell_in -= 1

        if sell_in < 0:
            if quality < 50:
                quality += 1
        return Item(name=item.name, sell_in=sell_in, quality=quality)

    def update_quality(self):
        for i, item in enumerate(self.items):
            new_item = Item(item.name, item.sell_in, item.quality)
            if item.name == "Aged Brie":
                new_item = self.handle_aged_brie(new_item)
                self.items[i] = new_item
                continue

            if item.name != "Backstage passes to a TAFKAL80ETC concert":
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
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if new_item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            new_item.quality = new_item.quality - 1
                else:
                    new_item.quality = 0

            self.items[i] = new_item

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
