"""Bag-of-Words (BoW) minimal demo — matches the book's two-sentence example.

Run:
  python 04_code_lab/bow_demo.py
"""


def tokenize(text: str) -> list[str]:
    return text.lower().split()


def build_vocabulary(corpus: list[str]) -> list[str]:
    """Preserve first-seen order (matches typical textbook BoW walkthroughs)."""
    vocab: list[str] = []
    seen: set[str] = set()
    for sentence in corpus:
        for token in tokenize(sentence):
            if token not in seen:
                seen.add(token)
                vocab.append(token)
    return vocab


def bow_vector(sentence: str, vocabulary: list[str]) -> list[int]:
    index = {token: i for i, token in enumerate(vocabulary)}
    vector = [0] * len(vocabulary)
    for token in tokenize(sentence):
        if token in index:
            vector[index[token]] += 1
    return vector


def main() -> None:
    s1 = "That is a cute dog"
    s2 = "My cat is cute"
    corpus = [s1, s2]
    vocab = build_vocabulary(corpus)

    print("Vocabulary:", vocab)
    print("Vector for:", repr(s2))
    print(bow_vector(s2, vocab))


if __name__ == "__main__":
    main()
