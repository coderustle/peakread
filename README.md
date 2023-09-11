# PeakRead: An NLP-Powered Article Summarizer.

A simple tool to get quick summaries of online articles. It uses `typer` to make commands easy and `newspaper3k` to grab and shorten articles, so you can understand the main points fast.

## Features:
1. **Swift Summaries**: Get to the heart of articles in mere seconds.
2. **NLP-Powered**: Leverages advanced Natural Language Processing algorithms.
3. **Simple CLI Interface**: Easy-to-use, perfect for both beginners and advanced users.

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install the required packages

## Requirements

**Debian/Ubuntu**
```bash

# Needed by lxml
sudo apt-get install libxml2-dev libxslt-dev

# needed by PIL
sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev
```

**OSX**
```bash
$ brew install libxml2 libxslt

$ brew install libtiff libjpeg webp little-cms2
```
## Usage

```bash
# download the NLTK models and corpora
$ peak init

# read and summarize an article
$ peak read --url url
```
