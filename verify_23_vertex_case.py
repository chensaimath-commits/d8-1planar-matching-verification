#!/usr/bin/env python3
"""Verify the 23-vertex triangle-incidence exclusion, (R,k,a)=(11,3,0)."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
CASE_DATA = ROOT / "verification_data" / "case23_triangle_incidence"


def main() -> None:
    subprocess.run(
        [
            sys.executable,
            "verify_23_quartic.py",
            "quartic23_F3x8_F4x17.plc",
        ],
        cwd=CASE_DATA,
        check=True,
    )
    print("PASS case 2: 23-vertex triangle-incidence exclusion")


if __name__ == "__main__":
    main()
