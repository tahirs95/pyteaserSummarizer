from pyteaser import Summarize


def summarize(title, content):
    return " ".join(Summarize(title, str(content)))
