names = ["Jeff", "Charlie", "James", "Nick", "James", "James"]


def remove_enemies(names, enemies):
    while enemies in names:
        k = names.index(enemies)
        names.pop(k)
    return names


names = remove_enemies(names, "James")
print(names)