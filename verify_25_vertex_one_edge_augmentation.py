#!/usr/bin/env python3
"""Verify the 25-vertex one-edge-augmentation exclusion, (R,k,a)=(12,3,1)."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "verification_data"
QUARTIC_DATA = DATA / "case25_quartic"
CORE_DATA = DATA / "case25_core"
PARALLEL_DATA = DATA / "case25_parallel"


def verify_quartic_branches() -> None:
    subprocess.run(
        [sys.executable, "verify_typeB25.py", "octa25c2.plc"],
        cwd=QUARTIC_DATA,
        check=True,
    )


def verify_common_core() -> None:
    compiler = shutil.which("cc")
    if compiler is None:
        raise SystemExit("A C99 compiler named 'cc' is required.")

    with tempfile.TemporaryDirectory(prefix="d8-case25-core-") as directory:
        checker = Path(directory) / "verify_core_superset"
        subprocess.run(
            [
                compiler,
                "-O3",
                "-std=c99",
                "-Wall",
                "-Wextra",
                "-Werror",
                "-DCORE_ACCEPT_SUPERSET",
                "-o",
                str(checker),
                str(CORE_DATA / "verify_core_duals.c"),
            ],
            check=True,
        )
        environment = os.environ.copy()
        environment["D8_CORE_SUPERSET_VERIFIER"] = str(checker)
        subprocess.run(
            [sys.executable, "verify_superset_manifest.py"],
            cwd=CORE_DATA,
            env=environment,
            check=True,
        )


def verify_parallel_branch() -> None:
    subprocess.run(
        [sys.executable, "verify_manifest.py"],
        cwd=PARALLEL_DATA,
        check=True,
    )


def main() -> None:
    verify_quartic_branches()
    verify_common_core()
    verify_parallel_branch()
    print("PASS case 4: 25-vertex one-edge-augmentation exclusion")


if __name__ == "__main__":
    main()
