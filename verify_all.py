#!/usr/bin/env python3
"""Run the four finite exclusions used in the d=8 proof."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
PROGRAMS = (
    "verify_19_vertex_case.py",
    "verify_23_vertex_case.py",
    "verify_25_vertex_zero_augmentation.py",
    "verify_25_vertex_one_edge_augmentation.py",
)


def main() -> None:
    for number, program in enumerate(PROGRAMS, 1):
        print(
            f"\n=== Running verification {number} of {len(PROGRAMS)}: {program} ===",
            flush=True,
        )
        subprocess.run([sys.executable, str(ROOT / program)], check=True)
    print("\nPASS all four finite exclusions", flush=True)


if __name__ == "__main__":
    main()
