def calc_o(x, y, counter, verbose=False):
    r = 0
    for index in range(0, counter):
        r = r + (index+1)*(x+y)
        if verbose:
            print(f"#{index}, r={r}")
    print(f"calc_o({x}, {y})={r}")
    return r


if __name__ == "__main__":
    r = calc_o(10, 2, 4, verbose=True)
    r = calc_o(10, 2, 4, verbose=False)
