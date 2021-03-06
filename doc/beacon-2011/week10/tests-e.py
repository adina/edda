def fn2(x, item):
    # put code in here to satisfy tests below
    pass

###

# test code

# test 1
somelist = []
newlist = fn2(somelist, "tuna")

assert len(somelist) == 0
assert len(newlist) == 1
assert "tuna" in newlist

# test 2
somelist = ["tuna"]
newlist = fn2(somelist, "ahi")

assert "tuna" in newlist
assert "ahi" in newlist
assert "ahi" not in somelist

assert len(somelist) == 1, somelist
assert len(newlist) == 2, somelist

# test 3
somelist = ["tuna", "ahi"]
newlist = fn2(somelist, "ahi")

assert "tuna" in newlist
assert "ahi" in newlist

assert len(somelist) == 2, somelist
assert len(newlist) == 2, somelist
