import requests
from requests.exceptions import RequestException
from flask import Flask, render_template, request


from extractor import ContentExtractor
from summarizer import summarize

app = Flask(__name__)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        if "url" in request.form and request.form["url"]:
            # Checking if url is in the form.
            url = request.form["url"]
            title = ""
            summary = ""
            images = []
            try:
                res = requests.get(url, headers=HEADERS)  # requesting the url.
            except RequestException:
                title = "Failed to fetch the article content from given link."

            if res.status_code == 200:
                html_content = res.content

                extractor = ContentExtractor(html_content)
                content = extractor.content()
                title = extractor.title()
                images = extractor.images()

                summary = summarize(title, str(content))

            else:
                title = "Page not found."

            return render_template("form.html", data={"summary": summary, "title": title, "images": images})

    return render_template("form.html", data={"summary": "", "title": ""})


app.run(debug=True)
