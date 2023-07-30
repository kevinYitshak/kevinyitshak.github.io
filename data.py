from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class Person:
    name: str
    picture_url: str
    email: str
    # twitter: str
    website: str
    github: str
    # linkedin: str
    # google_scholar: str
    biography: str
    interests: list[str] | None = None
    address: str | None = None
    phone: str | None = None


@dataclass(kw_only=True, slots=True)
class Position:
    title: str
    description: str
    from_date: str
    to_date: str


@dataclass(kw_only=True, slots=True)
class Employment:
    company: str
    location: str
    periods: list[Position]

@dataclass(kw_only=True, slots=True)
class Education:
    institution: str
    degree: str
    location: str
    from_date: str
    to_date: str
    text: str


@dataclass(kw_only=True, slots=True)
class ResearchExperience:
    institution: str
    project: str
    location: str
    from_date: str
    to_date: str
    text: str


@dataclass(kw_only=True, slots=True)
class Publication:
    title: str
    nickname: str
    year: str
    authors: list[str]
    venue: str
    resources: dict[str, str]

@dataclass(kw_only=True, slots=True)
class Project:
    title: str
    nickname: str
    resources: dict[str, str]

@dataclass(kw_only=True, slots=True)
class Talk:
    pass


@dataclass(kw_only=True, slots=True)
class Teaching:
    pass


@dataclass(kw_only=True, slots=True)
class MediaAppearance:
    pass


@dataclass(kw_only=True, slots=True)
class Service:
    pass



BIOGRAPHY = """
Previously, I was a <b>Research Assistant</b> at Spectrum Lab,
<b>IISc</b>, India under the supervision of <i>Chandra Sekhar</i>. 
During which I got an oppertunity to work on multiple projects
related to image processing and computer vision for Bio-medical images. 
<br>
I finished my undergraduate degree in Electrical and Electronics Engineering
with a minor specialization in signal processing and control from Manipal Institute of Technology, India.
"""

INTRO = """
I am a Master student at <b>Saarland University</b> working on <b>3D Reconstruction</b> with <i>Eddy Ilg</i> and <i>Jan Eric Lennsen</i>.
"""

INTERESTS = [
    "computer graphics",
    "machine learning",
    "neural representations",
    "geometry learning",
    "computer vision",
]

PERSON = Person(
    name="Kevin Yitshak",
    picture_url="kevin.jpg",
    email="kepe00001@stud.uni-saarland.de",
    website="https://kevinyitshak.github.io",
    github="https://github.com/kevinYitshak",
    # linkedin="https://www.linkedin.com/in/ana-dodik-246bb0150/",
    # google_scholar="https://scholar.google.com/citations?user=cDmCKFcAAAAJ&sortby=pubdate",
    biography=BIOGRAPHY,
    interests=INTERESTS,
    address="",
    phone="",
)

PUBLICATIONS = [
    Publication(
        title="Automatic Classification of Artery-Vein from a Single Wavelength Fundus Images",
        nickname="av-classification",
        authors=["P. Kevin Raj" , "Aniketh Manjunath", "J.R.H. Kumar", "Chandra S. Seelamantula"],
        year="2020",
        venue="IEEE International Symposium on Biomedical Imaging (ISBI), Iowa, USA.",
        resources={
            "paper": "publication/av-classification/",
            "supplementary": "publication/av-classification/ISBI_2020_PPT.pdf",
            "bibtex": "publication/av-classification/cite.bib",
        },
    ),
    Publication(
        title="A Structure Tensor based Voronoi Decomposition Technique for Optic Cup Segmentation",
        nickname="optic-cup-seg",
        authors=["P. Kevin Raj", "J.R.H Kumar", "S. Jois", "S. Harsha", "Chandra S. Seelamantula"],
        year="2019",
        venue="IEEE International Conference on Image Processing (ICIP), Taipei, Taiwan.",
        resources={
            "paper": "publication/optic-cup-seg/",
            "supplementary": "publication/optic-cup-seg/ICIP_PPT_19.pdf",
            "bibtex": "publication/optic-cup-seg/cite.bib",
        },
    ),
    Publication(
        title="Automatic Segmentation of Common Carotid Artery in Longitudinal Mode Ultrasound Images Using Active Oblongs",
        nickname="carotid-artery-seg",
        authors=["J.R.H. Kumar", "K. Teotia", "P. Kevin Raj", "A. Jasbon", "K.V. Rajagopal", "Chandra S. Seelamantula"],
        year="2019",
        venue="IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Brighton, UK.",
        resources={
            "paper": "publication/carotid-artery-seg/",
            "supplementary": "publication/carotid-artery-seg/",
            "bibtex": "publication/carotid-artery-seg/cite.bib",
        },
    ),
    # Publication(
    #     title="Path Guiding Using A Spatio-Directional Mixture Model",
    #     nickname="sdmm-paper",
    #     authors=["Ana Dodik", "Marios Papas", "Cengiz Öztireli", "Thomas Müller"],
    #     year="2021",
    #     venue="Computer Graphics Forum",
    #     resources={
    #         "paper": "publication/sdmm-paper/sdmm-paper.pdf",
    #         "supplementary": "publication/sdmm-paper/sdmm-paper-suppl.pdf",
    #         "code": "https://github.com/anadodik/sdmm-mitsuba",
    #         "thesis": "https://www.research-collection.ethz.ch/handle/20.500.11850/411118",
    #         "talk": "https://youtu.be/7D2r6K4rrqA?t=1774",
    #         "bibtex": "publication/sdmm-paper/dodik21pathguiding.bib",
    #         "video": "publication/sdmm-paper/sdmm-video.mp4",
    #         "interactive": "publication/sdmm-paper/website/index.html",
    #     },
    # ),
]

PROJECTS = [
    Project(
        title="Few-shot Semantic Segmentation of Wireless Capsule Endoscopy Images",
        nickname="wce-class",
        resources={
            "paper": "project/wce-class/paper.pdf",
            "code": "https://github.com/kevinYitshak/wce"
        }
    )
]

Employment(
    company="Meta",
    location="Zurich, Switzerland",
    periods=[
        Position(
            title="Computer Vision Engineer",
            description="Worked on 3D body reconstruction from images as part of the AR Commerce team. Co-supervised multiple research interns.",
            from_date="Sep 2020",
            to_date="May 2022",
        ),
        Position(
            title="Computer Vision Intern",
            description="Worked on grayscale image colorization using a hybrid machine-learning and optimization method. In collaboration with Facebook AI Research.",
            from_date="Jun 2019",
            to_date="Aug 2019",
        ),
    ],
)

Employment(
    company="Microsoft",
    location="Belgrade, Serbia",
    periods=[
        Position(
            title="Computer Vision Intern",
            description="Researched and prototyped a novel method for a video editing effect as part of the Bend Reality project.",
            from_date="Jul 2017",
            to_date="Sep 2017",
        ),
    ],
)

Education(
    institution="Massachusetts Institute of Technology",
    degree="PhD Computer Science",
    location="Cambridge, MA, USA",
    from_date="Jul 2022",
    to_date="ongoing",
    text="Presidential fellow. Working on neural representations for geometry processing. Co-advised by Justin Solomon and Vincent Sitzmann.",
)

Education(
    institution="ETH Zurich",
    degree="MSc Computer Science",
    location="Zurich, Switzerland",
    from_date="Sep 2017",
    to_date="Apr 2020",
    text="Focus on computer graphics, machine learning, and computer vision.",
)

Education(
    institution="Vienna University of Technology",
    degree="BSc Software and Information Engineering",
    location="Vienna, Austria",
    from_date="Oct 2014",
    to_date="Jul 2017",
    text="German language preparation course in 2013/2014. GPA 1.50 (≈3.80 USA GPA).",
)

Education(
    institution="United World College in Mostar",
    degree="Bilingual International Baccalaureate Diploma",
    location="Mostar, Bosnia and Herzegovina",
    from_date="Sep 2011",
    to_date="May 2013",
    text="",
)

ResearchExperience(
    institution="ETH Zurich, CGL, collaboration with Disney Research Studios and Nvidia Research.",
    project="Master's Thesis",
    location="Zurich, Switzerland",
    from_date="Sep 2018",
    to_date="May 2019",
    text="\"Path Guiding using a Spatio-Directional Mixture Model\"",
)

ResearchExperience(
    institution="Disney Research Zurich",
    project="Semester Project and Research Internship",
    location="Zurich, Switzerland",
    from_date="Jul 2018",
    to_date="Sep 2018",
    text="Researching strategies for guiding light paths and sampling BSDFs during rendering.",
)

ResearchExperience(
    institution="ETH Zurich, CVG",
    project="Research assistant",
    location="Zurich, Switzerland",
    from_date="Nov 2017",
    to_date="Sep 2018",
    text="Applying machine learning to 3D geometry reconstruction from video.",
)

ResearchExperience(
    institution="Vienna University of Technology, Rendering and Modeling Group",
    project="Bachelor's Thesis",
    location="Vienna, Austria",
    from_date="Jan 2017",
    to_date="Aug 2017",
    text="\"Implementing Probabilistic Connections for Bidirectional Path Tracing in The Mitsuba Renderer.\"",
)

ResearchExperience(
    institution="Vienna University of Technology, Rendering and Modeling Group",
    project="Undergraduate research assistant",
    location="Vienna, Austria",
    from_date="Jan 2016",
    to_date="Aug 2017",
    text="Literature review and work on a CUDA implementation for image-space filtering of Monte Carlo rendering noise.",
)