def maximum_score(tile_hand):
    b = []
    f = 0
    for i in tile_hand:
        a = tile_hand[f]
        c = a.get("score")
        f += 1
        b.append(c)
    return sum(sorted(b)[-7:])


lst = [
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]


print(maximum_score(lst))
print(str(1//2))