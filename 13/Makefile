COURSES := NAIL062 NDBI025 NDMI002 NDMI011 NJAZ070 NJAZ072 NJAZ074 NJAZ090 NJAZ091 NMAI054 NMAI057 NMAI058 NMAI059 NMAI069 NPRG030 NPRG031 NPRG045 NPRG062 NSWI120 NSWI141 NSWI170 NSWI177 NTIN060 NTIN061 NTIN071 NTVY014 NTVY015 NTVY016 NTVY017


public_html/index.html: src/index.md
        pandoc -o index.html index.md

index.html : _menu.md
	@echo "nieco" > public_html/index.html

_menu.md : _menu.md
	@echo "nieco" > _menu.md

_menu.html: _menu.md
        pandoc -o $@ $^

clean:
	@/bin/rm -f public_html/*.html
	@/bin/rm -f public_html/*.css
	@/bin/rm -f '_menu*'

