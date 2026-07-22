#!/bin/env python

from pathlib import Path
import requests
import os
import ads

ADS_TOKEN = os.environ["ADS_DEV_KEY"]


def get_ads_library(library_id, num_rows):
    return list(
        ads.SearchQuery(
            q=f"docs(library/{library_id}) property:refereed",
            fl=[
                "bibcode",
                "title",
                "author",
                "date",
                "doi",
                "pub",
                "year",
                "abstract",
                "eprint",
                "volume",
                "page",
                "identifier",
            ],
            rows=num_rows,
        )
    )


def get_citation_strings(bibcodes):
    headers = {
        "Authorization": f"Bearer {ADS_TOKEN}",
        "Content-Type": "application/json",
    }

    r = requests.post(
        "https://api.adsabs.harvard.edu/v1/export/aas",
        headers=headers,
        json={"bibcode": bibcodes},
    )

    r.raise_for_status()

    return r.json()["export"]


def format_author(name):
    parts = [p.strip() for p in name.split(",", 1)]
    if len(parts) == 2:
        last, first = parts
        return f"{first} {last}"
    return name


def format_authors(authors):
    authors = [format_author(a) for a in authors]

    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} & {authors[1]}"
    elif len(authors) == 3:
        return f"{authors[0]}, {authors[1]}, & {authors[2]}"
    else:
        return f"{authors[0]}, {authors[1]}, {authors[2]}, et al."


def format_citation(p):
    authors = format_authors(p.author)
    year = p.year
    journal = p.pub
    volume = getattr(p, "volume", "")
    page = getattr(p, "page", [""])[0]
    return (
        f"{authors} ({year}), {journal} {volume} {page} DOI:{p.doi[0]}"
    )


def get_arxiv_id(paper):
    for identifier in getattr(paper, "identifier", []):
        if identifier.startswith("arXiv:"):
            return identifier.removeprefix("arXiv:")
    return None


papers = get_ads_library(library_id="IfGigYrbQvyqn94YRYC7Xw", num_rows=50)
papers.sort(key=lambda p: int(p.year), reverse=True)


def paper_as_md(paper):
    date = paper.date[:10]
    citation = format_citation(paper)
    arxivid = get_arxiv_id(paper)
    return f"""---
title: "{paper.title[0]}"
collection: publications
permalink: /publication/{date}-{arxivid}.html
date: {date}
venue: '{paper.pub}'
paperurl: https://doi.org/{paper.doi[0]}
citation: '{citation}.'
---
{paper.abstract}.

[Preprint](https://arxiv.org/abs/{arxivid})
"""


def save_paper_md(paper, output_dir="."):
    """Save a paper as a Markdown file."""

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    date = paper.date[:10]
    filename = output_dir / f"{date}-{paper.bibcode}.md"

    filename.write_text(paper_as_md(paper), encoding="utf-8")

    return filename


for paper in papers:
    save_paper_md(paper, output_dir="../_publications")
