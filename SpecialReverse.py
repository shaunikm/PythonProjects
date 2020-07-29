def special_reverse(s, c):
    return ' '.join(m[::-1] if m[0] == c else m for m in s.split())


print(special_reverse('word searches are super fun', 's'))