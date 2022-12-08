from typing import Dict, List


def get_word_frequencies(doc: str) -> Dict[str, int]:
    """Extracts word frequencies from a document.

    Args:
        doc: Document content given as a string.

    Returns:
        Dictionary with words as keys and their frequencies as values.
    """
    # TODO
    ...


def get_word_feature_vector(
    word_frequencies: Dict[str, int], vocabulary: List[str]
) -> List[int]:
    """Creates a feature vector for a document, comprising word frequencies
        over a vocabulary.

    Args:
        word_frequencies: Dictionary with words as keys and frequencies as
            values.
        vocabulary: List of words.

    Returns:
        List of length `len(vocabulary)` with respective frequencies as values.
    """
    # TODO
    ...
