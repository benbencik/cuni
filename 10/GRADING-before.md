# Before class quiz for 10 (student bencikb)

| Total                                            |    92 |
|--------------------------------------------------|------:|
| Q1 (previous lab)                                |    25 |
| Q2 (disk image creation)                         |    25 |
| Q3 (signals in Python)                           |    21 |
| Q4 (disk mounting)                               |    21 |

If you see an issue with the grading, please
[open a **Confidential Issue**](https://gitlab.mff.cuni.cz/teaching/nswi177/2022/common/forum/-/issues/new?issue[confidential]=true&issue[title]=Grading+Before+class+quiz+for+10)
in the _Forum_.


For assignments with automated tests you will see a TAP-style result output
that you are familiar with from your pipeline tests in GitLab.

The tests also contains information about points assigned (or subtracted)
for that particular test. There are also tests with _zero points_ that
are informative only (kind of like warnings from your compiler: you
should pay attention but they are not crucial).

## Q1 (previous lab)

**Points**: 25


## Q2 (disk image creation)

**Points**: 25

**Expected:** 3 (answered 3)


## Q3 (signals in Python)

**Points**: 21

**Expected:** 1, 2, 5, 6, 8 (answered 1, 2, 6, 8)


### General notes (collected from all solutions)

Few more notes to signal handling and signals in general.

The truth is that even us were surprised at the number of corner cases
that we can encounter only when launching the toy examples from the labs.

Key thing to remember: signals are really asynchronous. They can
occur at really any time and even innocent looking code such as
the following can be interrupted "in the middle".

```python
i = i + 1
```

That is, the instructions executed can really be "read current value of i
and increment it by 1", "handle signal that just arrived" (and after a long
time) "store the updated value of i".

In this sense, the code depicted in question Q3 also contained few places
where signals can cause quite unexpected behaviour.

For example, sending SIGHUP quickly followed by SIGTERM might mean that
SIGTERM would be ignored. It would come during `load_configuration` and
the `signal_received` flag would be lost (overwritten).

The expected answers targeted the naive interpretation because during the labs
even that proved to be complicated enough :-). We have accepted and gave
points also for answers that would be correct in the stricter interpretation.

Unfortunately, there is no easy way out. Writing 100% safe code with respect
to signals is very difficult but at least for some languages, such as C,
the Linux documentation states how the function behaves with respect to
signal handling (e.g. whether it can be interrupted, what it means or whether
it is possible to call it from a signal handler). Higher level languages
are often silent about such issues completely.

As a last thing, if we return to our shell example.

```shell
my_temp="$( mktemp )"

trap on_exit ...
```

Even this is wrong. Because the signal can arrive before `trap` is called,
hence the file might remain undeleted. But switching the ordering means
that the handler might be called before the file was created and we should
check that `my_temp` is set. But again, the file might have been created
but its name was not yet printed. Etc. etc.

So perhaps, the above is good enough as empty temporary file is relatively
innocent :-)


## Q4 (disk mounting)

**Points**: 21

**Expected:** 1, 4, 6 (answered 4, 6)


