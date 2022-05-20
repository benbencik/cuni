# Tasks 12 (student bencikb)

| Total                                            |    70 |
|--------------------------------------------------|------:|
| 12/csv_calc.sh                                   |    40 |
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

✅ **Submitted** (passed, informative only)

✅ **Proper shebang** (passed, +0 points)

✅ **Executable bit** (passed, +0 points)

✅ **Shellcheck errors** (passed, +0 points)

✅ **Shellcheck warnings** (passed, +0 points)

✅ **Shellcheck infos** (passed, informative only)

✅ **Shellcheck stylistic** (passed, informative only)

✅ **Pre-flight check** (passed, +10 points)

❌ **Pre-flight check for non-zero exit code** (failed, worth 10 points) \

```
-- Program exit code mismatch --
actual   : 0
expected : 1
--
```

❌ **Pre-flight check for code injection** (failed, worth 10 points) \

```
-- precious.txt is gone, injection in expression is possible --
path : /tmp/nswi177-tests/precious.txt
--
```

✅ **Malicious data injection on master branch** (passed, informative only)

✅ **Issue for code injection exists** (passed, +10 points)

✅ **Issue for code injection has reasonable description** (passed, +5 points)

✅ **Issue for code injection contains some code example** (passed, +5 points)

❌ **Malicious data injection fixed in branch** (failed, worth 10 points) \

```
You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.
If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:
  git switch -c <new-branch-name>
Or undo this operation with:
  git switch -
Turn off this advice by setting config variable advice.detachedHead to false
HEAD is now at 78223eb idk2
-- precious3.txt is gone, injection in data is possible --
path : /tmp/nswi177-tests/precious3.txt
--
```

✅ **Malicious data injection closes the issue** (passed, +10 points)



## 12/UPSTREAM.md

✅ **Exists** (passed, informative only)

✅ **Properly merged** (passed, +30 points)



