from jinja2 import Environment, FileSystemLoader

from data import PERSON, INTRO, PUBLICATIONS

RESOURCE_ICONS = {
    "paper": "fa-solid fa-file-pdf",
    "supplementary": "fa-solid fa-file-pdf",
    "code": "fa-solid fa-code",
    "thesis": "fa-solid fa-file-pdf",
    "presentation": "bi bi-file-earmark-slides-fill",
    "bibtex": "fa-solid fa-quote-right",
    "video": "fa-solid fa-video",
    "talk": "fa-solid fa-video",
    "interactive": "fa fa-arrow-pointer",
    "website": "fa-solid fa-arrow-up-right-from-square",
}

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
        publications=PUBLICATIONS,
        resource_icons=RESOURCE_ICONS,
        resource_readable_names=RESOURCE_READABLE_NAMES,
    )
    with open("index.html", mode="w", encoding="utf-8") as file:
        file.write(content)