def colour_trio(colours: str):
    """
    This problem was inspired by the Mathologer video “Secret of Row 10”. To start, assume the exis-
tence of three values called “red”, “yellow” and “blue”. These names serve as colourful (heh)
mnemonics and could as well have been 0, 1, and 2, or “foo”, “bar” and “baz”; no connection to actual
physical colours is implied. Next, de5ine a rule to mix such colours so that mixing any colour with
itself gives that same colour, whereas mixing any two different colours always gives the third colour.
For example, mixing blue to blue gives that same blue, whereas mixing blue to yellow gives red,
same as mixing yellow to blue, or red to red.
Given the first row of colours as a string of lowercase letters, this function should construct the
rows below the first row one row at the time according to the following discipline. Each row is one
element shorter than the previous row. The i:th element of each row comes from mixing the colours
in positions i and i + 1 of the previous row. Rinse and repeat until only the singleton element of the
bottom row remains, returned as the 5inal answer. For example, starting from 'rybyr' leads to
'brrb', which leads to 'yry', which leads to 'bb', which leads to 'b' for the 5inal answer, Regis.
When the Python virtual machine laughs and goes 'brrrrr', that will lead to 'yrrrr', 'brrr',
'yrr', and 'br' for the 5inal answer 'y' for “Yes, please!”
    """
    def mix(str1, str2):
        if str1 == str2:
            return str1
        color_list = ['r', 'y', 'b']
        for color in color_list:
            if color not in (str1, str2):
                return color

    if len(colours) == 1:
        return colours

    new_colors = ''
    for i in range(len(colours) - 1):
        new_colors += mix(colours[i], colours[i+1])

    return colour_trio(new_colors)


print('y', colour_trio('y'))
print('rr', colour_trio('rr'))
print('bb', colour_trio('bb'))
print('rybyr', colour_trio('rybyr'))
print('rybyry', colour_trio('rybyry'))
print('brybbr', colour_trio('brybbr'))
print('rbyryrrbyrbb', colour_trio('rbyryrrbyrbb'))
print('yrbbbbryyrybb', colour_trio('yrbbbbryyrybb'))
