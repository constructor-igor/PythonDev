import logging
import inspect
import traceback
import json

def get_function_parameters_and_values():
    func_name = traceback.extract_stack(None, 2)[0][2]
    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)
    func_args_str = ", ".join([f"{i}={str(values[i])}" for i in args])
    args_as_dict = values
    return func_name, args_as_dict, f"{func_name}({func_args_str})"

    # args = locals()
    # keys = list(args.keys())
    # keys.reverse()
    # func_name = inspect.currentframe().f_code.co_name
    # args_str = ", ".join([f"{key}={args[key]}" for key in keys])
    # logging.info(f"{func_name}({args_str})")

def calc_n(x, y, counter):
    func_name, args_as_dict, args_as_str = get_function_parameters_and_values()
    logging.info(f"{args_as_str}")
    with open(f'{func_name}_input.json', 'w') as fp:
        json.dump(args_as_dict, fp)

    if counter==0:
        logging.warn(f"counter == {counter}")
    r = 0
    for index in range(0, counter):
        r = r + (index+1)*(x+y)
        logging.debug(f"#{index}, r={r}")
    logging.info(f"calc_o({x}, {y}, {counter})={r}")
    return r


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    calc_n(1, 2, 3)
    calc_n(1, 2, 0)