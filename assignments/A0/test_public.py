import A1_1 as module


def test_get_word_frequencies_1():
    """This test is 0.5 points."""
    doc = "and with great power\ncomes great responsibility\nand few vacations"
    frequencies = {
        "with": 1,
        "great": 2,
        "power": 1,
        "comes": 1,
        "responsibility": 1,
        "and": 2,
        "few": 1,
        "vacations": 1,
    }
    assert module.get_word_frequencies(doc) == frequencies


def test_get_word_frequencies_2():
    """This test is 0.5 points."""
    doc = (
        "document.with, punctuation:   with?spaces\ttabs\nwith newslines\n\n\n"
    )
    frequencies = {
        "with": 3,
        "document": 1,
        "punctuation": 1,
        "spaces": 1,
        "tabs": 1,
        "newslines": 1,
    }
    assert module.get_word_frequencies(doc) == frequencies


def test_get_word_feature_vector_1():
    """This test is 0.5 points."""
    frequencies = {
        "with": 1,
        "great": 2,
        "power": 1,
        "comes": 1,
        "responsibility": 1,
        "and": 2,
        "few": 1,
        "vacations": 1,
    }
    vocabulary = list(sorted(frequencies))
    feature_vector = [2, 1, 1, 2, 1, 1, 1, 1]
    assert (
        module.get_word_feature_vector(frequencies, vocabulary)
        == feature_vector
    )


def test_get_word_feature_vector_2():
    """This test is 0.5 points."""
    frequencies = {
        "with": 3,
        "document": 1,
        "punctuation": 1,
        "spaces": 1,
        "tabs": 1,
        "newslines": 1,
    }
    vocabulary = ["document", "spaces", "tabs", "with", "great", "power"]
    feature_vector = [1, 1, 1, 3, 0, 0]
    assert (
        module.get_word_feature_vector(frequencies, vocabulary)
        == feature_vector
    )
