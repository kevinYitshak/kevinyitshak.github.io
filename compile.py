from jinja2 import Environment, FileSystemLoader

from data import PERSON, BIOGRAPHY, INTRO, INTERESTS, PUBLICATIONS, PROJECTS

RESOURCE_READABLE_NAMES = {
    "paper": "Paper",
    "supplementary": "Supplementary",
    "code": "Code",
    "thesis": "Thesis",
    "presentation": "Presentation",
    "bibtex": "BibTeX",
    "video": "Video",
    "talk": "Talk",
    "interactive": "Interactive Results",
    "website": "Project Website",
}

if __name__ == "__main__":
    environment = Environment(loader=FileSystemLoader("templates"))
    template = environment.get_template("index.html")
    content = template.render(
        person=PERSON,
        intro=INTRO,
        bio=BIOGRAPHY,
        interests=INTERESTS,
        publications=PUBLICATIONS,
        projects=PROJECTS,
        resource_readable_names=RESOURCE_READABLE_NAMES,
    )
    with open("index.html", mode="w", encoding="utf-8") as file:
        file.write(content)
