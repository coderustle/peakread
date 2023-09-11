import nltk
import typer
from newspaper import Article

app = typer.Typer()


REQUIRED_CORPORA = [
    "brown",  # Required for FastNPExtractor
    "punkt",  # Required for WordTokenizer
    "maxent_treebank_pos_tagger",  # Required for NLTKTagger
    "movie_reviews",  # Required for NaiveBayesAnalyzer
    "wordnet",  # Required for lemmatization and Wordnet
    "stopwords",
]


@app.command()
def init():
    """
    Downloads the necessary NLTK models and corpora required to support all of newspaper's features.
    """
    for each in REQUIRED_CORPORA:
        print(('Downloading "{0}"'.format(each)))
        nltk.download(each)
    print("Finished.")


@app.command()
def peak(url: str):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    with open(f"{article.title}.txt", "w") as f:
        f.write(article.summary)


if __name__ == "__main__":
    app()
