# Computer verification for the $d=8$ case

This repository contains the computer code used to verify the four finite
cases arising in the proof of the sharp edge bound for simple 1-planar graphs
with bounded matching number and maximum degree at most seven.  In the
notation of the paper, this is the case $d=8$.

For a factor-critical block $H$, write

```text
|V(H)| = 2R+1,        |E(H)| = 7R+k,
```

and let $a$ be the number of uncrossed edges added when the planarization is
completed to a triangulation.  The theoretical argument in the paper reduces
the remaining possibilities to the following four parameter triples.

## The four verification programs

| Program | $(\nu,k,a)$ | Finite case | Decisive recorded value |
|---|---:|---|---:|
| `verify_19_vertex_case.py` | $(9,2,0)$ | 19-vertex dual-matching exclusion | `complete_matchings=0` |
| `verify_23_vertex_case.py` | $(11,3,0)$ | 23-vertex triangle-incidence exclusion | `target_tau_1x22_2=0` |
| `verify_25_vertex_zero_augmentation.py` | $(12,3,0)$ | 25-vertex zero-augmentation exclusion | `type_B=0`, `exact_patch_phases=0` |
| `verify_25_vertex_one_edge_augmentation.py` | $(12,3,1)$ | 25-vertex one-edge-augmentation exclusion | all residual counts are zero |

A zero in the last column means that the corresponding hypothetical block
does not exist.

## Code structure

- `verify_19_vertex_case.py` checks the 19-vertex case.
- `verify_23_vertex_case.py` checks the 23-vertex case.
- `verify_25_vertex_zero_augmentation.py` checks the 25-vertex case with
  $a=0$.
- `verify_25_vertex_one_edge_augmentation.py` checks the 25-vertex case with
  $a=1$.
- `verify_all.py` runs all four programs in the order shown above.
- `verification_data/` contains the recorded exhaustive-search catalogues,
  source files, logs, hashes, and low-level independent checkers.  It is kept
  in one directory so that the repository home page remains simple.

The two 25-vertex cases share part of the same quartic-map and common-core
enumerations.  The public programs are nevertheless separated because they
exclude different mathematical configurations.

## Prerequisites

The recorded verification requires

- Python 3.9 or later;
- a C99 compiler available as `cc`; and
- a POSIX-compatible system such as Linux or macOS.

The Python programs use only the standard library.  No package installation
is required.

## Running the code

Run all four verifications from the repository root:

```sh
python3 verify_all.py
```

Run one verification separately, for example:

```sh
python3 verify_23_vertex_case.py
```

A successful complete run ends with

```text
PASS all four finite exclusions
```

Any malformed input, changed source or catalogue hash, failed structural
test, or nonzero residual count terminates the relevant program with a
nonzero exit status.

## Reproducibility

The public programs recompile the C checkers when needed and independently
validate the recorded catalogues, search logs, and final zero counts.  This
provides a practical verification of the checked-in certificates.

The command `python3 verify_all.py` does not repeat the most expensive
exhaustive catalogue generation and inverse enumeration.  Their generation
commands, source provenance, reference counts, and SHA-256 values are recorded
in the technical notes inside `verification_data/`.

## Citation

This repository accompanies the paper *Maximum Size of 1-Planar Graphs with
Maximum Degree Seven and Bounded Matching Number*.  Citation metadata are
provided in `CITATION.cff`.

## Licensing notice

No repository-wide license has yet been selected for the authors' original
code.  The repository also contains third-party plantri sources, which remain
subject to their upstream terms.  See `LICENSE-NOTICE.md` and the license
notices stored with those sources.
