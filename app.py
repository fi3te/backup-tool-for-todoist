import api
import data_io


def main() -> None:
    data_obj, data_dict = api.load()
    file_name = data_io.new_file_name_without_file_extension()
    data_io.dump_json(file_name, data_dict)
    data_io.dump_csv(file_name, data_obj)
    print('Backup created!')


if __name__ == '__main__':
    main()
