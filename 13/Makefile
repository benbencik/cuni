#!/bin/bash

set -ueo pipefail
set -x

COURSES = NAIL062 NDBI025 NDMI002 NDMI011 NJAZ070 NJAZ072 NJAZ074 NJAZ090 NJAZ091 NMAI054 NMAI057 NMAI058 NMAI059 NMAI069 NPRG030 NPRG031 NPRG045 NPRG062 NSWI120 NSWI141 NSWI170 NSWI177 NTIN060 NTIN061 NTIN071 NTVY014 NTVY015 NTVY016 NTVY017

build_page() {
    local page="$1"
    shift

    pandoc --template template.html -B _menu.html "src/${page}.md" "$@" > "public_html/${page}.html"
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

clean: 
