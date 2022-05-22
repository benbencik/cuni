#!/bin/bash

set -ueo pipefail
set -x

build_page() {
    local page="$1"
    shift

    pandoc \
        --template template.html \
        -B _menu.html "src/${page}.md" \
        "$@" \
        > "public_html/${page}.html"
}

(
    echo '* [Homepage](index.html)'
    ./bin/make_menu.sh src/N*.meta
) >_menu.md

pandoc _menu.md >_menu.html

build_page "index"
for course_meta in src/N*.meta; do
    course="$( basename "${course_meta}" .meta )"
    build_page "${course}" --metadata-file "${course_meta}"
done

cp main.css public_html
