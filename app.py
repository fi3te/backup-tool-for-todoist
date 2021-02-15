import argh

import api
import constants
import data_io


@constants.add_parameter
def main() -> None:
    data_obj, data_dict = api.load()
    file_name = data_io.new_file_name_without_file_extension()
    data_io.dump_json(file_name, data_dict)
    if data_obj is not None:
        data_io.dump_csv(file_name, data_obj)
        print('Backup created!')
    else:
        print('Unexpected server response!')


if __name__ == '__main__':
    argh.dispatch_command(main)
