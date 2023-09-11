from bs4 import BeautifulSoup


def get_main_contents(html_content, template):
    with open(html_content, "r", encoding="utf-8") as file:
        content = file.read()
    with open(template, "r", encoding="utf-8") as temp:
        to_fill = temp.read()
    soup = BeautifulSoup(to_fill, "html.parser")
    print(soup.prettify())


get_main_contents(html_content="test.html", template="experiment.html")
