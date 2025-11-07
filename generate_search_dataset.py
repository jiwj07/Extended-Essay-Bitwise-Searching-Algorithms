# make_search_datasets.py
import csv
import random
import os
from pathlib import Path

def make_and_save_sorted_dataset(n: int, bits: int, seed: int, filename: str, base_dir: Path):
    """Generate a sorted dataset of n unique random integers and save to a CSV file."""
    random.seed(seed)
    max_val = 2**bits - 1
    if n > max_val:
        raise ValueError(f"Cannot generate {n} unique values with {bits} bits (max {max_val}).")

    data = random.sample(range(max_val + 1), n)
    data.sort()

    filepath = base_dir / filename
    with filepath.open(mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["value"])
        for val in data:
            writer.writerow([val])

    print(f"Generated sorted dataset of {n} unique {bits}-bit integers -> {filepath}")


if __name__ == "__main__":
    try:
        base_dir = Path(__file__).resolve().parent
    except NameError:
        base_dir = Path.cwd()

    BITS = 32
    BASE_SEED = 12345

    sizes = [100, 10_000, 1_000_000]
    variants = [1, 2, 3, 4, 5]

    for n in sizes:
        for i in variants:
            seed = BASE_SEED + i * 100 + n
            filename = f"{n}_dataset_{i}.csv"
            make_and_save_sorted_dataset(n, BITS, seed, filename, base_dir)