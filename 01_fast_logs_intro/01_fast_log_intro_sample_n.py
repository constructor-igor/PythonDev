import logging


def calc_n(x, y, counter):
    r = 0
    for index in range(0, counter):
        r = r + (index+1)*(x+y)
        logging.debug(f"#{index}, r={r}")
    logging.info(f"[calc_n] f({x}, {y}, {counter}) = {r}")
    return r

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    r = calc_n(10, 2, 4)
    logging.getLogger().setLevel(logging.INFO)
    r = calc_n(1, 2, 4)