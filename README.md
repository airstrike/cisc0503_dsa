# CISC 0503 Data Structures and Algorithms

This package contains solutions and implementations for the assignments in the CISC 0503 Data Structures and Algorithms course.

## Project Structure

```
.
├── html/...
│   ├── coverage/
│   ├── docs/
│   └── index.html
├── src/
│   └── cisc0503_dsa/
│       ├── buffer.py
│       ├── stack.py
│       └── ...other modules
├── tests/...
├── build.sh
├── clean_coverage.py # used by build.sh
├── LICENSE
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Assignments

Each assignment in the course corresponds to a tagged release in this repository. For example, the solutions for the first assignment can be found under the `assignment-01` tag.

## Installation

To install the package, you can use pip or simply copy the contents of the `src/cisc0503_dsa` directory into your project.

*Note: The package is not currently available on PyPI. I'll upload it when I have some extra time...*

```
pip install cisc0503_dsa
```

## Usage

After installation, you can import and use the module as follows:

```python
from cisc0503_dsa import BufferArray
```

## Testing

To run all tests, you can use the following command:

```
coverage run -m unittest discover tests
```

Or if you don't have `coverage` installed, simply:

```
python -m unittest discover tests
```

You may also run individual tests by specifying the test file name. For example,
to run the tests for the `Stack` class, you can cd into the `tests` directory and
use the following command:

```
python -m test_Stack
```

Each test file generally tests only one set of class variants. For example,
the `test_SortedBufferArray` file tests "sorted buffers" classes, which are
`SortedBufferArrayWithDups` and `SortedBufferArrayNoDups`. Tests for the base
`BufferArray` class are in the `test_BufferArray` file.

## Test Coverage

To generate a coverage report after running tests with `coverage`, run the following command:

```
coverage html --directory ./html/coverage
```

The test coverage requires the `coverage` package, which can be installed using pip
with the following command:

```
pip install coverage
```

## Building the Documentation

To build the documentation, you can use the following command:

```
pdoc --html --force --output-dir ./html/docs ./src/
```

Note: The documentation is already built and included in the `docs` directory. Building it from source requires the `pdoc3` package, which can be installed using pip:

```
pip install pdoc3 # to install the latest pdoc3 from PyPI
pip install -r requirements.txt # to install the exact version used in this project
```

## Building the Project

To test the project, build docs and report coverage in one go in a *nix OS, you can
use the `build.sh` script:

```
./build.sh
```

If the build process fails, pass the `--verbose` flag to figure out why:

```
./build.sh --verbose
```

Mac OS: You may also pass an `--open-docs` flag to open the generated docs in your default browser:

```
./build.sh --open-docs # this simply calls "open ./html/index.html"
```

## License

This project is licensed under the "unlicense" terms of the included LICENSE file.
