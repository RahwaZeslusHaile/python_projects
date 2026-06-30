from lineup_students import lineup_students


def test_lineup_students_long_words():
    assert lineup_students(
        "Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi"
    ) == [
        "Takehiko",
        "Takayuki",
        "Takahiro",
        "Takeshi",
        "Takeshi",
        "Takashi",
        "Tadashi",
        "Takeo",
        "Takao",
    ]

def test_lineup_students_short_words():
    assert lineup_students("xxa xxb xxc xxd xa xb xc xd") == [
        "xxd",
        "xxc",
        "xxb",
        "xxa",
        "xd",
        "xc",
        "xb",
        "xa",
    ]

def test_lineup_students_empty_list():
    assert lineup_students(['']) == []