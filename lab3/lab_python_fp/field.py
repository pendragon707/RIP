def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for dict in items:
            yield dict[args[0]]
    else:
        new_dict = {}
        for dict in items:
            for key in args:
                try:
                    new_dict[key] = dict[key]
                except KeyError:
                    continue
            yield new_dict
            new_dict.clear()
