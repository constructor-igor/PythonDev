import warnings

def calc_o(x, y, counter, verbose=False):
    if counter==0:
        warnings.warn(f"counter == {counter}")
    r = 0
    for index in range(0, counter):
        r = r + (index+1)*(x+y)
        if verbose:
            print(f"#{index}, r={r}")
    print(f"calc_o({x}, {y}, {counter})={r}")
    return r


if __name__ == "__main__":
    r = calc_o(1, 2, 4, verbose=True)
    r = calc_o(2, 3, 5, verbose=False)
    r = calc_o(2, 3, 0)
