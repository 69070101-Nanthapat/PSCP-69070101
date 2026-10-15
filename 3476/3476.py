""" CuteCat CuteFox """

import ast

def main():
    """CuteCat CuteFox"""
    n = int(input())
    pets = {}
    for _ in range(n):
        d = ast.literal_eval(input())
        for k in d:
            pets[k] = d[k]
    codes = set(pets.values())
    if "Cat01" not in codes and "Garfield" not in pets:
        pets["Garfield"] = "Cat01"
    if "Fox01" not in codes and "Fubuki" not in pets:
        pets["Fubuki"] = "Fox01"
    cats = [(v, k) for k, v in pets.items() if v.startswith("Cat")]
    foxes = [(v, k) for k, v in pets.items() if v.startswith("Fox")]
    cats.sort(key=lambda t: int(t[0][3:]))
    foxes.sort(key=lambda t: int(t[0][3:]))
    print(f"Cat : {len(cats)}")
    print(f"Fox : {len(foxes)}")
    for v, k in cats:
        print(f"{k} : {v}")
    for v, k in foxes:
        print(f"{k} : {v}")

main()
