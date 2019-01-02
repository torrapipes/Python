def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:        # Comienzo de la etiqueta
            tag = True
        elif c == '>' and not quote:      # Fin de la etiqueta
            tag = False
        elif (c == '"' or c == "'") and tag:
        # Pasamos (o salimos) al estado quote
            quote = not quote
        elif not tag:
            out = out + c
    assert out.find('<')==-1, "tag en out"
    return out

print(remove_html_markup('"<'))
print(remove_html_markup('<a href="don\'t">link</a>'))
print(remove_html_markup('<b>foo</b>'))
print(remove_html_markup('<b>"foo"</b>'))
print(remove_html_markup('"<b>foo</b>"'))
print(remove_html_markup('<"b">foo</"b">'))