from collections import defaultdict
from dataclasses import dataclass
import re

@dataclass
class bag_type:
    name: str
    contents: dict

'''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''

BAG_TYPE_DIR = {}

# Bag type parser
bag_type_parser = re.compile(r'(?P<bag_name>.*) bags?')
content_option_parser = re.compile(r'(?P<bag_count>\d+) (?P<bag_name>.*) bags?')
#field_pair_parser = re.compile(r'(?P<bag_name>\d+)(?P<bag_name>.*):(?P<value>.*)')

def init_bag_type(name):
    global BAG_TYPE_DIR
    if name not in BAG_TYPE_DIR:
        BAG_TYPE_DIR[name] = {
            'parent_options': set(),
            'content_options': {}
        }

def parse_rules_file(filename):
    global BAG_TYPE_DIR
    with open(filename) as f:
        lines = f.read().splitlines()
    for line in lines:
        bag_type, content_rules =line.split(" contain ")
        m = bag_type_parser.match(bag_type)
        containing_bag = m.group('bag_name')
        init_bag_type(containing_bag)

        if content_rules != 'no other bags.':
            content_options = content_rules.split(", ")
            for option in content_options:
                m = content_option_parser.match(option)
                count = int(m.group('bag_count'))
                contained_bag = m.group('bag_name')
                init_bag_type(contained_bag)
                assert contained_bag not in BAG_TYPE_DIR[containing_bag]['content_options']
                BAG_TYPE_DIR[containing_bag]['content_options'][contained_bag] = count
                BAG_TYPE_DIR[contained_bag]['parent_options'].add(containing_bag)

def get_possible_containers(name):
    assert name in BAG_TYPE_DIR
    possible_containers = set()
    new_bags = {name}
    while new_bags:
        new_bag = new_bags.pop()
        possible_containers.add(new_bag)
        new_bags |= (BAG_TYPE_DIR[new_bag]['parent_options'] - possible_containers)
    possible_containers.remove(name)
    return possible_containers


def get_contents_count(name):
    assert name in BAG_TYPE_DIR
    total = 0
    for contained_bag, count in BAG_TYPE_DIR[name]['content_options'].items():
        total += count * (1 + get_contents_count(contained_bag))
    return total

if __name__ == '__main__':
    parse_rules_file('./7/input.txt')
    possible_containers = get_possible_containers('shiny gold')
    print(len(possible_containers))
    print(get_contents_count('shiny gold'))