import os
import shutil
from pathlib import Path

from bs4 import BeautifulSoup


def scan_tree(path=".", item_wanted=None):
    want_dirs = True
    want_files = True
    if item_wanted == "dirs":
        want_files = False
    elif item_wanted == "files":
        want_dirs = False
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scan_tree(entry.path, item_wanted=item_wanted)
            if want_dirs:
                yield entry
        else:
            if want_files:
                yield entry


def setup_working_file(working_file):
    template = "templates/template.html"
    with open(template, "r", encoding="utf-8") as temp:
        content = temp.read()
    with open(working_file, "w", encoding="utf-8") as w:
        w.write(content)


def set_title(title, working_file):
    with open(working_file, "r", encoding="utf-8") as r:
        content = r.read()
    soup = BeautifulSoup(content, "html.parser")
    soup.title.string.replace_with(title)
    with open(working_file, "w", encoding="utf-8") as w:
        w.write(str(soup.prettify()))


def set_heading(heading, working_file):
    with open(working_file, "r", encoding="utf-8") as r:
        content = r.read()
    soup = BeautifulSoup(content, "html.parser")
    h = soup.find(lambda tag: tag.name == "h2" and "HEADING" in tag.text)
    h.string.replace_with(heading)
    with open(working_file, "w", encoding="utf-8") as w:
        w.write(str(soup.prettify()))


def get_main_contents(working_file, html_content):
    with open(html_content, "r", encoding="utf-8") as file:
        content = file.read()
    filler_soup = BeautifulSoup(content, "html.parser")
    with open(working_file, "r", encoding="utf-8") as temp:
        to_fill = temp.read()
    soup = BeautifulSoup(to_fill, "html.parser")
    soup.find(id="main_section").insert(1, filler_soup)
    with open("output.html", "w", encoding="utf-8") as out:
        out.write(str(soup.prettify()))


def fill_page(working_file, html_content):
    working_file = "script-drafting.html"
    html_content = "test.html"
    file_name = " ".join(Path(html_content).stem.split("_")).capitalize()
    heading = f"Location: {file_name}"
    setup_working_file(working_file=working_file)
    set_title(title=file_name, working_file=working_file)
    set_heading(heading=heading, working_file=working_file)
    get_main_contents(working_file=working_file, html_content=html_content)


def clean_docs_and_move_resources():
    if os.path.exists("docs/maps"):
        shutil.rmtree("docs/maps")
    shutil.copytree("maps", "docs/maps")


def make_places():
    for i in scan_tree(path="places-html", item_wanted="files"):
        pass


clean_docs_and_move_resources()
