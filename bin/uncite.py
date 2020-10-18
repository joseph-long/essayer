import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

import yaml
from pybtex.database import parse_file

EXT = "md"

POSTS_DIRS = ["_posts", "_drafts"]
REVIEWS_DIRS = ["_books"]
PATH_MAP = {
    "_posts": "/{}.html",
    "_drafts": "/{}.html",
    "_books": "/bibliography/{}.html",
}
UNCITES_FP = "_data/uncites.yml"
SEE_ALSO_FP = "_data/see_alsos.yml"

CITE_REGEXP = "{% cite(_detail)? (?P<cite_keys>.*?)( -.*?)? %}"
POST_DATE_NAME_REGEXP = r"(\d{4}-\d{2}-\d{2}-)?(?P<post_name>.+)"

BIB_DIR = Path("_bibliography")
BIB_DATA = [parse_file(BIB_DIR / bib) for bib in os.listdir(BIB_DIR)]

YAML_KWARGS = dict(explicit_start=True, explicit_end=True, indent=2)


def main():
    cite_posts = defaultdict(set)

    for post_dir in POSTS_DIRS:
        posts = filter(lambda fn: fn.endswith(".md"), os.listdir(post_dir))
        for post in posts:
            post_date_name, _ = os.path.splitext(post)
            match = re.search(POST_DATE_NAME_REGEXP, post_date_name)
            if not match:
                continue
            post_name = match.groupdict()["post_name"]
            post_path = PATH_MAP[post_dir].format(post_name)
            with open(os.path.join(post_dir, post), "r") as f:
                post_contents = f.read().replace("\n", "")
            matches = re.finditer(CITE_REGEXP, post_contents)
            for match in matches:
                cite_keys = match.groupdict()["cite_keys"].split(" ")
                for cite_key in cite_keys:
                    if cite_key == post_name:
                        continue
                    cite_posts[cite_key] |= {post_path}
    with open(UNCITES_FP, "w") as f:
        uncites = {key: list(posts) for key, posts in cite_posts.items()}
        yaml.dump(uncites, f, **YAML_KWARGS)

    see_also_reviews = defaultdict(set)

    for reviews_dir in REVIEWS_DIRS:
        reviews = filter(
            lambda fn: fn.endswith(".md"), os.listdir(reviews_dir)
        )
        for review in reviews:
            review_date_name, _ = os.path.splitext(review)
            match = re.search(POST_DATE_NAME_REGEXP, review_date_name)
            if not match:
                continue
            review_cite_key = match.groupdict()["post_name"]
            with open(os.path.join(reviews_dir, review), "r") as f:
                review_contents = f.read().replace("\n", "")
            matches = re.finditer(CITE_REGEXP, review_contents)
            for match in matches:
                cite_keys = match.groupdict()["cite_keys"].split(" ")
                for cite_key in cite_keys:
                    if cite_key == review_cite_key:
                        continue
                    see_also_reviews[cite_key] |= {review_cite_key}
        with open(SEE_ALSO_FP, "w") as f:
            see_alsos = defaultdict(list)
            for key, reviews in see_also_reviews.items():
                for review_cite_key in reviews:
                    review_path = PATH_MAP[reviews_dir].format(review_cite_key)
                    review_title = next(
                        bib_data.entries[review_cite_key].fields["title"]
                        for bib_data in BIB_DATA
                        if review_cite_key in bib_data.entries
                    )
                    see_alsos[key].append(
                        {"title": review_title, "path": review_path}
                    )
            yaml.dump(dict(see_alsos), f, **YAML_KWARGS)


if __name__ == "__main__":
    main()
