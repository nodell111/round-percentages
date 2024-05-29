# Define your list of percentages
percentages = [13.626332, 47.989636, 9.596008, 28.788024]

# Call the round_percentages function
rounded_percentages = round_percentages(percentages, precision=1)

# Print the rounded percentages
print(rounded_percentages)


def round_percentages(percentages, precision=0):
    """
    Given an iterable of percentages that add up to 100, round them to the nearest integer such
    that the rounded percentages also add up to 100. Uses the largest remainder method.

    E.g.
    round_percentages([13.626332, 47.989636, 9.596008, 28.788024], precision=1) -> [14.0, 48.0, 9.0, 29.0]

    """
    result = []
    sum_of_integer_parts = 0

    for index, percentage in enumerate(percentages):
        integer_part = round(percentage, precision)
        decimal_part = round((percentage - integer_part) * (10 ** precision))

        result.append([integer_part, decimal_part, percentage - integer_part, index])
        sum_of_integer_parts += integer_part

    result.sort(key=lambda x: (x[2], x[1]), reverse=True)
    difference = 100 - sum_of_integer_parts

    for percentage in result:
        if difference == 0:
            break
        percentage[0] += 1
        difference -= 1

    # order by the original order
    result.sort(key=lambda x: x[3])

    # return just the percentage
    return [percentage[0] for percentage in result]
