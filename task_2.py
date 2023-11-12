import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def convert_csv_to_json(input_filename: str, output_filename: str) -> None:
    # Считать содержимое CSV файла
    with open(input_filename, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = [row for row in csv_reader]

    # Сериализовать в файл JSON с отступами равными 4
    with open(output_filename, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4, ensure_ascii=False)


def task() -> None:
    convert_csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
