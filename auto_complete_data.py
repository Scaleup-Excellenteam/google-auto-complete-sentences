from dataclasses import dataclass

@dataclass
class AutoCompleteData:
    """
    This class represents a single result of a search.

    Attributes:
        completed_sentence (str): The completed sentence.
        source_text (str): The source file of the completed sentence.
        offset (int): The offset of the sentence in the source text.
        score (int): The score of the sentence.
    """
    completed_sentence: str
    source_text: str
    offֵset: int
    score: int
