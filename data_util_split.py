import splitfolders

splitfolders.ratio(
    "ham_data/reorganized",
    output="ham_data/splitted_ham10000",
    seed=42,
    ratio=(.8, .0, .2),
    group_prefix=None,
    move=False
)