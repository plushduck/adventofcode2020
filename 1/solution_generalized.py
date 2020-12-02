from collections import Counter
import time
start_time = time.time()

product_of_addends_tests = [
    {
        "input": [0, 2020],
        "target": 2020,
        "solution": 0
    },
    {
        "input": [1010],
        "target": 2020,
        "solution": None
    },
    {
        "input": [1010, 1010],
        "target": 2020,
        "solution": 1010*1010
    }
]

test2 = sorted([1446, 1893, 1827, 1565, 1728, 497, 1406, 1960, 1986, 1945, 1731, 1925, 1550, 1841, 1789, 1952, 1610, 1601, 1776, 1808, 1812, 1834, 1454, 1729, 513, 1894, 1703, 1587, 1788, 1690, 1655, 1473, 1822, 1437, 1626, 1447, 1400, 1396, 1715, 1720, 1469, 1388, 1874, 1641, 518, 1664, 1552, 1800, 512, 1506, 1806, 1857, 1802, 1843, 1956, 1678, 1560, 1971, 1940, 1847, 1902, 1500, 1383, 1386, 1398, 1535, 1713, 1931, 1619, 1519, 1897, 1767, 1548, 1976, 1984, 1426, 914, 2000, 1585, 1634, 1832, 1849, 1665, 1609, 1670, 1520, 1490, 1746, 1608, 1829, 1431, 1762, 1384, 1504, 1434, 1356, 1654, 1719, 1599, 1686, 1489, 1377, 1531, 1912, 144, 1875, 1532, 1439, 1482, 1420, 1529, 1554, 1826, 1546, 1589, 1993, 1518, 1708, 1733, 1876, 1953, 1741, 1689, 773, 1455, 1613, 2004, 1819, 1725, 1617, 1498, 1651, 2007, 1402, 728, 1475, 1928, 1904, 1969, 1851, 1296, 1558, 1817, 1663, 1750, 1780, 1501, 1443, 1734, 1977, 1901, 1547, 1631, 1644, 1815, 1949, 1586, 1697, 1435, 1783, 1772, 1987, 1483, 1372, 1999, 1848, 1512, 1541, 1861, 2008, 1607, 1622, 1629, 1763, 1656, 1661, 1581, 1968, 1985, 1974, 1882, 995, 1704, 1896, 1611, 1888, 1773, 1810, 1650, 1712, 1410, 1796, 1691, 1671, 1947, 1775, 1593, 656, 1530, 1743])

call_count = 0

def product_of_addends(target, target_count, values, counts=None, used_counts=None):
    global call_count
    call_count += 1
    if target < 0:
        return None
    if counts is None:
        counts = Counter(values)
    if used_counts is None:
        used_counts = Counter()
    if target_count == 2:
        for v in values:
            unused = counts[v]-used_counts[v]
            if unused == 0:
                continue
            if v*2 == target and unused < 2:
                continue
            if (target-v) in values:
                return v*(target-v)
    else:
        for v in values:
            if used_counts[v] >= counts[v]:
                continue
            used_counts[v] += 1
            product = product_of_addends(target - v, target_count -1, values, counts, used_counts)
            if product:
                return v*product
            used_counts[v] -= 1

def test_product_of_addends():
    for test in product_of_addends_tests:
        assert(product_of_addends(test["target"], 2, test["input"]) == test["solution"])

if __name__ == "__main__":
    print("Running 4 digit test")
    print(product_of_addends(1986 + 1952 + 1446 + 1849, 4, test2))
    print("Running product_of_addends tests")
    test_product_of_addends()
    with open('./1/input.txt') as f:
        values = {int(v) for v in f}
    print("Part A:")
    print(product_of_addends(2020, 2, values))
    print("Part B:")
    print(product_of_addends(2020, 3, values))


print("--- %s seconds ---" % (time.time() - start_time))
print(f"{call_count} calls")