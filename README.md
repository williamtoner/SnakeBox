# SnakeBox

A snake-in-the-box of length **2944** in the 13-dimensional hypercube Q<sub>13</sub>.

The previous best known length in Q<sub>13</sub> was 2938 (T. Taylor, 2026).

| | |
|---|---|
| Dimension | 13 |
| Length | 2944 edges (2945 vertices) |
| Previous record | 2938 ([Taylor 2026](https://arxiv.org/abs/2609.27483); [records table](https://www.minortriad.com/snake/)) |
| Found | 11 October 2026 |
| Author | William Toner |

## The snake

[`q13_2944.txt`](q13_2944.txt) holds the snake as a transition sequence: one character
per edge, giving the coordinate flipped at that step, in base 36 (`0`-`9`, then
`a` = 10, `b` = 11, `c` = 12). The path starts at vertex 0.

The same string can be pasted into the analyzer on the
[snake-in-the-box records page](https://www.minortriad.com/snake/).

SHA-256 of `q13_2944.txt`:

```
1ca699239f0c421d057a9578bb4fb67bcea99de73c231f329366bb2fbfe5012b
```

## Verification

[`verify.py`](verify.py) checks that the sequence is a snake: every vertex is visited
once, and no two vertices that are not consecutive on the path are adjacent in the
hypercube. It uses only the Python standard library.

```bash
python3 verify.py q13_2944.txt
```

Expected output:

```
dimension n      = 13
vertices         = 2945 (all distinct)
chords           = 0 (induced path)
snake length     = 2944 edges
VALID
```

## How it was found

Taylor's 2938 is built recursively from snakes in lower dimensions, so it splits into
pieces that each fill a subcube of 9 or 10 dimensions. Holding the rest of the snake
fixed, we cleared one piece at a time and rebuilt it from scratch with a GPU simulated
annealing search, keeping the result when it was longer. Three such rebuilds each
added two edges: 2938 to 2940 to 2942 to 2944.

## License

MIT. See [LICENSE](LICENSE).
