import logging

def calc_n(x, y, counter):
    if counter==0:
        logging.warn(f"counter == {counter}")
    r = 0
    for index in range(0, counter):
        r = r + (index+1)*(x+y)
        logging.debug(f"#{index}, r={r}")
    logging.info(f"calc_o({x}, {y}, {counter})={r}")
    return r

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""
# %(name)s Name of log
# %(pathname)s Full pathname of the source file where the logging call was issued(if available).
# %(filename)s Filename portion of pathname.
# %(module)s Module (name portion of filename).
# %(funcName)s Name of function containing the logging call.
# %(lineno)d Source line number where the logging call was issued (if available).
    format_other = "%(asctime)s [%(levelname)-7s] %(message)s"
    format_warning = '%(asctime)s [%(levelname)-7s] %(message)s [%(filename)s:%(lineno)d] '

    FORMATS = {
        logging.DEBUG: format_other,
        logging.INFO: format_other,
        logging.WARNING: format_warning,
        logging.ERROR: format_other,
        logging.CRITICAL: format_other
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(CustomFormatter())
    logging.getLogger().addHandler(console_handler)

    r = calc_n(1, 2, 4)
    r = calc_n(2, 3, 5)
    r = calc_n(2, 3, 0)