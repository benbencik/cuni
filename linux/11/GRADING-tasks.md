# Tasks 11 (student bencikb)

| Total                                            |    98 |
|--------------------------------------------------|------:|
| 11/tapsum2json                                   |    98 |

If you see an issue with the grading, please
[open a **Confidential Issue**](https://gitlab.mff.cuni.cz/teaching/nswi177/2022/common/forum/-/issues/new?issue[confidential]=true&issue[title]=Grading+Tasks+11)
in the _Forum_.


For assignments with automated tests you will see a TAP-style result output
that you are familiar with from your pipeline tests in GitLab.

The tests also contains information about points assigned (or subtracted)
for that particular test. There are also tests with _zero points_ that
are informative only (kind of like warnings from your compiler: you
should pay attention but they are not crucial).

## 11/tapsum2json

✅ **Submitted** (passed, informative only)

✅ **Submitted** (passed, informative only)

✅ **Submitted** (passed, informative only)

✅ **Executable bits** (passed, +0 points)

✅ **Executable bits** (passed, +0 points)

✅ **Executable bits** (passed, +0 points)

✅ **Only reasonable files are committed** (passed, +10 points)

✅ **No input files** (passed, +10 points)

✅ **Single file, both tests passing** (passed, +10 points)

✅ **Single non-existent file** (passed, +10 points)

✅ **Single file with skipped tests** (passed, +10 points)

✅ **Single file with another skipped tests** (passed, +10 points)

✅ **Pipeline-like invocation** (passed, +10 points)

✅ **Filename with space** (passed, +10 points)

✅ **Filename with quote character** (passed, +10 points)

✅ **Test with bail out** (passed, +10 points)

❌ **Needless dependencies** (failed, 2 points subtracted) \

```
-- Expected only tap.py among dependencies --
output (244 lines):
  absl-py
  apparmor
  appdirs
  application-utility
  argon2-cffi
  argon2-cffi-bindings
  astroid
  astronomia
  asttokens
  astunparse
  attrs
  autopep8
  backcall
  beautifulsoup4
  bleach
  Brotli
  btrfsutil
  build
  cachetools
  caffeine-ng
  certifi
  cffi
  chardet
  chrome-gnome-shell
  cleverhans
  click
  cloudpickle
  comtypes
  configobj
  cycler
  dash
  dash-core-components
  dash-html-components
  dash-table
  dateparser
  deap
  debugpy
  decorator
  defusedxml
  dill
  discid
  distro
  dm-tree
  dnspython
  docutils
  easydict
  entrypoints
  et-xmlfile
  ewmh
  executing
  fasteners
  filelock
  Flask
  Flask-Compress
  Flask-MySQL
  flatbuffers
  fonttools
  future-typing
  gast
  GNOME-App-Folders-Manager
  google-auth
  google-auth-oauthlib
  google-pasta
  googleapis-common-protos
  graphviz
  greenlet
  grpcio
  gufw
  gym
  gym-notices
  h5py
  HydroErr
  idna
  importlib-metadata
  inflection
  ipykernel
  ipython
  ipython-genutils
  ipywidgets
  isort
  itsdangerous
  jedi
  Jinja2
  joblib
  jupyter
  jupyter-client
  jupyter-console
  jupyter-core
  jupyterlab-pygments
  jupyterlab-widgets
  keras
  Keras-Preprocessing
  kiwisolver
  layoutswitcherlib
  lazy-object-proxy
  LibAppArmor
  libclang
  libfdt
  lit
  louis
  mando
  manjaro-sdk
  Markdown
  MarkupSafe
  matplotlib
  matplotlib-inline
  mc-bin-client
  mccabe
  mistune
  mnist
  more-itertools
  mutagen
  nbclient
  nbconvert
  nbformat
  neat-python
  nest-asyncio
  netsnmp-python
  nose
  notebook
  npyscreen
  numpy
  oauthlib
  openpyxl
  opt-einsum
  ordered-set
  packaging
  pacman-mirrors
  pandas
  pandocfilters
  parso
  patsy
  pendulum
  pep517
  pexpect
  picard
  pickleshare
  Pillow
  Pint
  Pint-Pandas
  platformdirs
  plotly
  plottoolbox
  prometheus-client
  promise
  prompt-toolkit
  protobuf
  psutil
  ptyprocess
  pulsectl
  pure-eval
  pwquality
  pyaf
  pyasn1
  pyasn1-modules
  pycairo
  pycodestyle
  pycparser
  pydot
  pygame
  Pygments
  PyGObject
  PyJWT
  pylint
  PyMySQL
  pyparsing
  PyQt5
  PyQt5-sip
  pyrsistent
  PySide6
  pysmbc
  python-dateutil
  python-xlib
  pytz
  pytz-deprecation-shim
  pytzdata
  pyxdg
  PyYAML
  pyzmq
  qtconsole
  QtPy
  ranger-fm
  regex
  reportlab
  requests
  requests-file
  requests-oauthlib
  rsa
  rst2ansi
  scikit-learn
  scipy
  Send2Trash
  setproctitle
  shiboken6
  six
  sklearn
  soundconverter
  soupsieve
  SQLAlchemy
  stack-data
  statsmodels
  systemd-python
  tabulate
  tap.py
  tappy
  team
  tenacity
  tensorboard
  tensorboard-data-server
  tensorboard-plugin-wit
  tensorflow
  tensorflow-datasets
  tensorflow-gpu
  tensorflow-io-gcs-filesystem
  tensorflow-metadata
  tensorflow-probability
  termcolor
  terminado
  testpath
  tf-estimator-nightly
  threadpoolctl
  tldextract
  toml
  tomli
  tornado
  tqdm
  traitlets
  tstoolbox
  typical
  typing_extensions
  tzdata
  tzlocal
  ufw
  urllib3
  validate
  wcwidth
  webencodings
  Werkzeug
  widgetsnbextension
  wrapt
  xlrd
  XlsxWriter
  youtube-dl
  zipp
expected (1 lines):
  tap.py
--
```

✅ **Needless dependencies** (passed, +0 points)



### General notes (collected from all solutions)

Most of the setup issues were covered by tests and they enforced that
you created a proper Python package that is easily installable. Good job!

But we had to add a new test that checked that your configuration does not
install needless dependencies. It seems that some of you misunderstood the
whole lab and installed packages globally anyway. Therefore, some of your
`requirements.txt` contained packages for downloading YouTube videos or
packages for YAML _loading_ or all packages for the example `timestamp2iso`
extended with `tap.py`.

The purpose of virtualenv is to provide a _clean_ and _repeatable_ environment
for building Python projects. You should also ensure that there are no
unneeded dependencies.

We also noticed that some of you ignored other implicit challenges within
this task. We have noticed use of global variables, manual printing of JSON
output and similar omissions. Note that final tasks will be also graded
manually and we will subtract points for such code.

As for an example solution, the following passes all tests except the one
with bail-out (but the extension to properly parse the `plan` line to allow
for that is quite easy).

Especially notice that line `json.dump` by itself ensures proper quoting of
the output without any extra work (and it is part of standard Python library).

```python
TapSummary = namedtuple('TapSummary', ['filename', 'total', 'passed', 'skipped', 'failed'])

def get_summary(filename):
    total = 0
    passed = 0
    skipped = 0
    failed = 0
    
    parser = tap.parser.Parser()
    for line in parser.parse_file(filename):
        if line.category == "test":
            total = total + 1
            if line.skip:
                skipped = skipped + 1
            elif line.ok:
                passed = passed + 1
            else:
                failed = failed + 1
        #elif line.category == "diagnostic":
        #    pass
        #elif line.category == "plan":
        #    ...
        #elif line.category == "bail":
        #    ...
       
    return TapSummary(filename, total, passed, skipped, failed)

def main():
    summaries = []
    for filename in sys.argv[1:]:
        try:
            summary = get_summary(filename)
        except FileNotFoundError:
            print("File {} not found.".filename, file=sys.stderr)
            summary = TapSummary(filename, 0, 0, 0, 0)
        summaries.append(summary)

    output = {
        'summary': [
            {
                'filename': i.filename,
                'total': i.total,
                'passed': i.passed,
                'skipped': i.skipped,
                'failed': i.failed,
            }
            for i in summaries
        ],
    }
    json.dump(output, sys.stdout, indent=True)
```


