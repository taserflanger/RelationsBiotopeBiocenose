def testInterval(ref, val, epsilon):
    if val < ref - epsilon:
        print("Too low, must be between {a} and {b}".format(a = ref - epsilon, b = ref + epsilon))
        return False
    elif val > ref + epsilon:
        print("Too high, must be between {a} and {b}".format(a = ref - epsilon, b = ref + epsilon))
        return False
    else:
        return True