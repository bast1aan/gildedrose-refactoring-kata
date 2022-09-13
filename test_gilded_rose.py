import json
import subprocess
import unittest
from typing import List

from gilded_rose import Item, GildedRose


def jsonfiy_items(items: List[Item]) -> List:
    return [repr(item) for item in items]


class GildedRoseTest(unittest.TestCase):
    def test_gilded_rose(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        ]

        actual = [jsonfiy_items(items)]

        gilded_rose = GildedRose(items)

        for _ in range(20):
            gilded_rose.update_quality()
            actual.append(jsonfiy_items(items))

        with open('actual.json', 'w') as f:
            f.write(json.dumps(actual, indent=4))

        proc = subprocess.Popen(f"diff actual.json expected.json", stdout=subprocess.PIPE, shell=True)
        out, _ = proc.communicate()

        self.assertEqual("", out.decode())
