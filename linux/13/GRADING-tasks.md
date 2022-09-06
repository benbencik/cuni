# Tasks 13 (student bencikb)

| Total                                            |     0 |
|--------------------------------------------------|------:|
| 13/Makefile                                      |     0 |

If you see an issue with the grading, please
[open a **Confidential Issue**](https://gitlab.mff.cuni.cz/teaching/nswi177/2022/common/forum/-/issues/new?issue[confidential]=true&issue[title]=Grading+Tasks+13)
in the _Forum_.


For assignments with automated tests you will see a TAP-style result output
that you are familiar with from your pipeline tests in GitLab.

The tests also contains information about points assigned (or subtracted)
for that particular test. There are also tests with _zero points_ that
are informative only (kind of like warnings from your compiler: you
should pay attention but they are not crucial).

## 13/Makefile

✅ **Submitted** (passed, informative only)

✅ **Generated files not committed** (passed, +0 points)

❌ **Target for cleaning** (failed, worth 10 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Base build for index.html** (failed, worth 20 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Base build for COURSE.html** (failed, worth 10 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Base build for main.css** (failed, worth 10 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Incremental build for template.html** (failed, worth 10 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Incremental build of index.html** (failed, worth 5 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Incremental build of main.css** (failed, worth 5 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Incremental build of course pages** (failed, worth 10 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Rebuild on meta information change** (failed, worth 10 points) \

```
-- Expecting make to terminate with success --
actual (1 lines):
  2
expected (1 lines):
  0
stdout (2 lines):
  make: Entering directory '/tmp/nswi177-tests/data/13'
  make: Leaving directory '/tmp/nswi177-tests/data/13'
stderr (1 lines):
  make: *** No rule to make target 'public_html/main.css', needed by 'all'.  Stop.
command (1 lines):
  make -C 13
--
```

❌ **Rebuild after adding new course** (failed, worth 10 points)

✅ **Code smells - Shellcheck** (passed, +0 points)



### General notes (collected from all solutions)

Generally, the solutions were good, there are only few points worth
mentioning.

Do not be afraid to use variables, even in Makefiles. They allow you to
capture the intent of a complex `addsufix/prefix` constructs, thus making
it easier for a reader.

It is a good idea to also manually test that what you have generated
makes sense. There were several solutions where the tests passed but the
generated HTML was total garbage (the tests could have been better, but
we simply did not expect that you would not open the generated page
at all).

Prefer to use `$@` even for simple targets. It simplifies further updates
when you decide to rename a file etc.

We expected that the solution would be somehow similar to the following
snippet (shortened).

```make
COURSES = ...

OUT_DIR = public_html

COURSE_PAGES = $(addprefix $(OUT_DIR)/,$(addsuffix .html, $(COURSES)))
OUT_FILES = $(OUT_DIR)/index.html $(OUT_DIR)/main.css $(COURSE_PAGES)

all: $(OUT_FILES)

$(OUT_DIR)/index.html: src/index.md template.html _menu.html
    pandoc --template template.html -B _menu.html $< >$@

$(OUT_DIR)/%.html: src/%.md template.html _menu.html
    pandoc --template template.html --metadata-file src/$*.meta -B _menu.html $< >$@

clean:
    rm -f public_html/* _menu.md _menu.html

...
```


