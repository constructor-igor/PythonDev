import os
import logging
import logging.handlers

def calc_n(x, y, counter):
    if counter==0:
        logging.warn(f"counter == {counter}")
    r = 0
    for index in range(0, counter):
        r = r + (index+1)*(x+y)
        logging.debug(f"#{index}, r={r}")
    logging.info(f"calc_o({x}, {y}, {counter})={r}")
    return r


def config_file_log(file_path, create_new=False, file_level=logging.DEBUG):
    logging.getLogger().setLevel(logging.DEBUG)
    if create_new:
        file_handler = logging.handlers.RotatingFileHandler(file_path, mode='w', backupCount=1)
    else:
        file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)-7s] %(message)s"))
    logging.getLogger().addHandler(file_handler)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    experiment_folder = os.path.dirname(__file__)
    experiment_log_file = os.path.join(experiment_folder, "experiment.log")
    config_file_log(experiment_log_file, create_new=True, file_level=logging.DEBUG)
    calc_n(1, 2, 3)
    calc_n(1, 2, 4)