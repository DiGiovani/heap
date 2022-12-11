from .heap import heap_sort
from pathlib import Path
import cProfile, csv

order_arr = ["crescente.csv", "decrescente.csv", "random.csv"]
size_arr = ["1000", "2000", "3000", "5000"]


for size in size_arr:
    print(f"CURRENT SIZE -> {size}")
    for order in order_arr:
        dataset = []

        print(f"CURRENT ORDER -> {order}")
        with open(f"{Path().absolute()}/datasets/{size}/{order}") as file:
            reader = csv.reader(file)
            header = next(file)
            for row in file:
                dataset.append(row.replace("\n", "").split(","))
        cProfile.run("heap_sort(dataset)")