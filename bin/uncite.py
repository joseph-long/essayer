import os
import re
import shutil
from collections import defaultdict

import yaml

EXT = "md"

POSTS_DIRS = ["_posts", "_drafts"]
UNCITES_FP = "_data/uncites.yml"

CITE_REGEXP = "{% cite(_detail)? (?P<cite_keys>.*?)( -.*)? %}"
POST_DATE_NAME_REGEXP = r"\d{4}-\d{2}-\d{2}-(?P<post_name>.+)"

UNCITE_TEMPLATE = """---
key: {cite_key}
posts: {posts}
---
"""


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
            with open(os.path.join(post_dir, post), "r") as f:
                post_contents = f.read().replace("\n", "")
            match = re.search(CITE_REGEXP, post_contents)
            if not match:
                continue
            cite_keys = match.groupdict()["cite_keys"].split(" ")
            for cite_key in cite_keys:
                cite_posts[cite_key] |= {post_name}
    with open(UNCITES_FP, "w") as f:
        yaml.dump(
            {key: list(posts) for key, posts in cite_posts.items()},
            f,
            explicit_start=True,
            explicit_end=True,
            indent=2,
        )


if __name__ == "__main__":
    main()
