#! /usr/bin/python3

import os
import sys
import subprocess
from pprint import pprint
import arrow
from six import u

now = arrow.now()
blog_dir = '/home/sandip/work/myblog'
post_template = \
"""---
layout:     post
title:      %s
date:       %s
author:     "Sandip Bhagat"
---
"""

def red(words):
    return u("\033[31m\033[49m%s\033[0m") % words

def teal(words):
    return u("\033[36m\033[49m%s\033[0m") % words

# remove the space and convert into lowercase
def normalize(text):
    return text.strip().lower()

# generate a post title
def generate_post_title(text):
    return normalize(text).title()

# generate a slug
def generate_slug(text):
    return normalize(text).replace(' ', '-')

# create new blog post
def create_new_post(text):
    post_title = generate_post_title(text)
    post_slug = generate_slug(text)
    file_name = "%s-%s.md" % (str(now.date()), post_slug)

    file_path = os.path.join(blog_dir, '_posts', file_name)
    template = post_template

    print("%s %s" % (teal("Creating file: "), file_path))
    post = open(file_path, 'w')
    post.write(template % (post_title, now.format('YYYY-MM-DD HH:mm Z')))
    post.close()
    subprocess.call(['subl', file_path])

# list all blog post in choronological order
def list_posts():
    pprint(sorted(os.listdir(os.path.join(blog_dir, '_posts')), reverse=True))

# fuck the app
def main():
    args = sys.argv[1:]

    # create new post
    if args[0] == 'new':
        create_new_post(args[1])

    # list all post
    elif args[0] == 'list':
        list_posts()

    # create slug
    elif args[0] == 'slug':
        print(generate_slug(args[1]))

    # create title
    elif args[0] == 'title':
        print(generate_post_title(args[1]))

    # create blog title and slug
    elif args[0] == 'st':
        print(generate_post_title(args[1]))
        print(generate_slug(args[1]))

    # print utc date and time according locale
    elif args[0] == 'dt':
        print(teal('Today: ' + now.format('YYYY-MM-DD HH:mm Z')))

# is this app genuine ???
if __name__ == '__main__':
    main()