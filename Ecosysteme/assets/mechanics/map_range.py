"""MapRange: module containing mapRange def"""

def map_range(value, left_min, left_max, right_min, right_max):
    """Returns a float given a *value* mapped and constrained between
    the value's min and max and the output min and max."""
    if value < left_min:
        return right_min
    if value > left_max:
        return right_max
    # Figure out how 'wide' each range is
    left_span = left_max - left_min
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (float)
    value_scaled = float(value - left_min) / float(left_span)

    # Convert the 0-1 range into a value in the right range.
    return right_min + (value_scaled * right_span)
