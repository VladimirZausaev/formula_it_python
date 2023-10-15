# TODO Найдите количество книг, которое можно разместить на дискете
v = 1.44
page_count = 100
str_count = 50
symbol_count = 25
one_symbol_weight = 4


v_in_bytes = v * 1024 ** 2
one_book_weight = one_symbol_weight * symbol_count * str_count * page_count
book_count = int(v_in_bytes // one_book_weight)
print("Количество книг, помещающихся на дискету:", book_count)
