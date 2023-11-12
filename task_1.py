# TODO решите задачу
import json


def task() -> float:
    f = open("input.json", "r")
    data = json.load(f)

    result = 0
    for item in data:
        result += item["score"] * item["weight"]
    return (round(result,3))

print(task())