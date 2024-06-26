def roundinglargerem(percentages, precision=0):
    unrounded = [x / float(sum(percentages)) * 100 * 10 ** precision for x in percentages]
    decimal_part_with_index = sorted([(index, unrounded[index] % 1) for index in range(len(unrounded))], key=lambda y: y[1], reverse=True)
    remainder = 100 * 10 ** precision - sum([int(x) for x in unrounded])
    index = 0
    while remainder > 0:
        unrounded[decimal_part_with_index[index][0]] += 1
        remainder -= 1
        index = (index + 1) % len(percentages)
    return [int(x) / float(10 ** precision) for x in unrounded]