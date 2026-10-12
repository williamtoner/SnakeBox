# SnakeBox

Record-length snakes-in-the-box in the 13- and 14-dimensional hypercubes, by William Toner.

| Dimension | Length | Previous best known | Found |
|---|---|---|---|
| 13 | **2946** edges | 2938 ([Taylor 2026](https://arxiv.org/abs/2609.27483)) | 11 October 2026 |
| 14 | **5850** edges | 5844 ([Taylor 2026](https://arxiv.org/abs/2609.27483)) | 12 October 2026 |

The 13-dimensional record is listed on the
[snake-in-the-box records page](https://www.minortriad.com/snake/), which covers
dimensions up to 13.

## The snakes

| File | Dimension | Length | SHA-256 |
|---|---|---|---|
| [`q14_5850.txt`](q14_5850.txt) | 14 | 5850 | `41ba6cebbc8bc8d029cfb93ae22f6a746a8bbb1fa99efca00591c9444606ee28` |
| [`q13_2946.txt`](q13_2946.txt) | 13 | 2946 | `56676e1993ab2d74c03a3ebe2e5668194379f2bd79839689e0b0e0daec79f795` |
| [`q13_2944.txt`](q13_2944.txt) | 13 | 2944 | `1ca699239f0c421d057a9578bb4fb67bcea99de73c231f329366bb2fbfe5012b` |

Each file holds a snake as a transition sequence: one character per edge, giving the
coordinate flipped at that step, in base 36 (`0`-`9`, then `a` = 10, `b` = 11, `c` = 12,
`d` = 13). The path starts at vertex 0. The 2944 was found first; the 2946 improves on it.

The 13-dimensional strings can be pasted into the analyzer on the records page.

## Verification

[`verify.py`](verify.py) checks that a sequence is a snake: every vertex is visited
once, and no two vertices that are not consecutive on the path are adjacent in the
hypercube. It uses only the Python standard library.

```bash
python3 verify.py q14_5850.txt
```

Expected output:

```
dimension n      = 14
vertices         = 5851 (all distinct)
chords           = 0 (induced path)
snake length     = 5850 edges
VALID
```

## How they were found

Taylor's snakes are built recursively from snakes in lower dimensions, so they split
into pieces that each fill a subcube of 9 or 10 dimensions. Holding the rest of the
snake fixed, we cleared one piece at a time and rebuilt it from scratch with a GPU
simulated annealing search, keeping the result when it was longer.

In 13 dimensions, three such rebuilds each added two edges: 2938 to 2940 to 2942 to
2944. Rebuilding also produced many different snakes of length 2944. On one of them,
an exact constraint-programming search over a 50-60 edge window found a reroute two
edges longer, giving 2946.

In 14 dimensions, rebuilding three pieces of Taylor's 5844 added two edges each:
5844 to 5846 to 5848 to 5850.

## License

MIT. See [LICENSE](LICENSE).
