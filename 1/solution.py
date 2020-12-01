def product_of_addends(target, values):
    for v in values:
        if (target-v) in values:
            return v*(target-v)

if __name__ == "__main__":
    with open('./1/input.txt') as f:
        values = {int(v) for v in f}
    print("Part A:")
    print(product_of_addends(2020, values))
    print("Part B:")
    for v in values:
        product = product_of_addends(2020 - v, values)
        if product:
            print(v * product)
            break
