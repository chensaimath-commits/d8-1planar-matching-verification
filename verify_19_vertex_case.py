#!/usr/bin/env python3
"""Verify the 19-vertex dual-matching exclusion, (R,k,a)=(9,2,0)."""

from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parent
CASE_DATA = ROOT / "verification_data" / "case19_dual_matching"


def main() -> None:
    compiler = shutil.which("cc")
    if compiler is None:
        raise SystemExit("A C99 compiler named 'cc' is required.")

    with tempfile.TemporaryDirectory(prefix="d8-case19-") as directory:
        checker = Path(directory) / "verify_19_skeletons"
        subprocess.run(
            [
                compiler,
                "-O3",
                "-std=c99",
                "-Wall",
                "-Wextra",
                "-Werror",
                "-o",
                str(checker),
                str(CASE_DATA / "verify_19_skeletons.c"),
            ],
            check=True,
        )
        subprocess.run(
            [str(checker), str(CASE_DATA / "tri19_4567.plc")],
            check=True,
        )

    print("PASS case 1: 19-vertex dual-matching exclusion")


if __name__ == "__main__":
    main()
