# Templater (final task 22) (student bencikb)

| Total                                            |   420 |
|--------------------------------------------------|------:|
| Manual evaluation (and comments)                 |    20 |
| Templater (automated tests)                      |   400 |

If you see an issue with the grading, please
[open a **Confidential Issue**](https://gitlab.mff.cuni.cz/teaching/nswi177/2022/common/forum/-/issues/new?issue[confidential]=true&issue[title]=Grading+Templater+(final+task+22))
in the _Forum_.


For assignments with automated tests you will see a TAP-style result output
that you are familiar with from your pipeline tests in GitLab.

The tests also contains information about points assigned (or subtracted)
for that particular test. There are also tests with _zero points_ that
are informative only (kind of like warnings from your compiler: you
should pay attention but they are not crucial).

## Manual evaluation (and comments)

**Points**: 20

Overall a good solution.

This requirements.txt certainly does not come from a clean virtual environment.

The spelling is `entry` not `enrty_point`.

Naming asymmetry between `jinja_filter_liters_to_gallons` and your new function.

Control flow in arabic numerals conversion function is too complicated (perhaps prefer EAFP, see https://stackoverflow.com/q/12265451).

Do not use numerical file descriptors if you can use symbolic ones (i.e. `sys.stderr` instead of `2`).

Switch `-V` would not work for values with equals sign (`-V var=a=b`).


## Templater (automated tests)

✅ **Submitted** (passed, informative only)

✅ **Submitted** (passed, informative only)

✅ **Submitted** (passed, informative only)

✅ **Executable bits** (passed, +0 points)

✅ **Executable bits** (passed, +0 points)

✅ **Executable bits** (passed, +0 points)

✅ **Only reasonable files are committed** (passed, +0 points)

✅ **Simple template** (passed, +40 points)

✅ **Gallons conversion** (passed, +25 points)

✅ **List in header** (passed, +20 points)

✅ **Example from README** (passed, +25 points)

✅ **arabic2roman 12** (passed, +35 points)

✅ **arabic2roman 2022** (passed, +15 points)

✅ **arabic2roman negative** (passed, +20 points)

✅ **arabic2roman non-number** (passed, +20 points)

✅ **US gallons conversion** (passed, +80 points)

✅ **Custom variables I** (passed, +60 points)

✅ **Custom variables II** (passed, +60 points)



