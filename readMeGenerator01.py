import jinja2
from jinja2 import FileSystemLoader
import os

env = jinja2.Environment(loader=FileSystemLoader("./templates/"))
template = env.get_template("README_template.md")


content= template.render({"RAG_INTRO_NB":"hi"})


with open("README2.md", mode="w", encoding="utf-8") as output:
    output.write(content)