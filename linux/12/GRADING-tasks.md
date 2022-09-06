# Tasks 12 (student bencikb)

| Total                                            |   100 |
|--------------------------------------------------|------:|
| 12/csv_calc.sh                                   |    70 |
| 12/UPSTREAM.md                                   |    30 |

If you see an issue with the grading, please
[open a **Confidential Issue**](https://gitlab.mff.cuni.cz/teaching/nswi177/2022/common/forum/-/issues/new?issue[confidential]=true&issue[title]=Grading+Tasks+12)
in the _Forum_.


For assignments with automated tests you will see a TAP-style result output
that you are familiar with from your pipeline tests in GitLab.

The tests also contains information about points assigned (or subtracted)
for that particular test. There are also tests with _zero points_ that
are informative only (kind of like warnings from your compiler: you
should pay attention but they are not crucial).

## 12/csv_calc.sh

✅ **Issue for code injection exists with correct marker** (passed, +10 points)

❌ **Issue for code injection has non-empty title** (failed, worth 10 points) \

```
-- Issue title should summarize the bug --
iid      : 2
title    : [task-malicious]
--
```

✅ **Issue for code injection has reasonable description** (passed, +5 points)

✅ **Issue for code injection contains some code example** (passed, +5 points)

✅ **Branch related to the issue exists with a correct name** (passed, +10 points)

✅ **Possible branch related to the issue found** (passed, informative only)

✅ **Branch closes the issue** (passed, +10 points)

❌ **Malicious data injection fixed in issue branch** (failed, worth 10 points) \

```
-- precious3.txt is gone, injection in data is possible --
path : /tmp/nswi177-tests/precious3.txt
--
```

✅ **Malicious data injection fixed as a separate commit** (passed, +10 points)

✅ **Base version imported** (passed, +10 points)

✅ **Exit code issue fixed - bad expression** (passed, +10 points)

❌ **Code injection in expression fixed** (failed, worth 10 points) \

```
-- No expression-injection resistant version of csv_calc.sh found --
Found following commits, but none of them provides
a csv_calc.sh fix injection-in-expression fixed.
 - 117ae5b2929de6053c89d829b2c877dcd6573b91 adding csv_calc.sh
--
```

✅ **Executable** (passed, +0 points)

✅ **Shellcheck errors** (passed, +0 points)

✅ **Shellcheck warning** (passed, +0 points)



## 12/UPSTREAM.md

✅ **Exists** (passed, informative only)

✅ **Properly merged** (passed, +30 points)



