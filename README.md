# CISC 0503 Data Structures and Algorithms

This package contains solutions and implementations for the assignments in the CISC 0503 Data Structures and Algorithms course.

## Project Structure

```
.
├── docs/...
├── src/
│   └── cisc0503_dsa/
│       ├── buffer.py
│       ├── buffer_ext.py
│       └── sorted_buffer.py
├── tests/...
├── build.sh
├── LICENSE
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Assignments

Each assignment in the course corresponds to a tagged release in this repository. For example, the solutions for the first assignment can be found under the `assignment-01` tag.

## Installation

To install the package, you can use pip or simply copy the contents of the `src/cisc0503_dsa` directory into your project.

```
pip install cisc0503_dsa
```

## Usage

After installation, you can import and use the module as follows:

```python
from cisc0503_dsa import BufferArray
```

## Testing

To run the tests, you can use the following command:

```
python -m unittest discover tests
```

## Building the Documentation

To build the documentation, you can use the following command:

```
pdoc --html --force --output-dir ./docs ./src/
```

Note: The documentation is already built and included in the `docs` directory. Building it from source requires the `pdoc3` package, which can be installed using pip:

```
pip install pdoc3 # to install the latest pdoc3 from PyPI
pip install -r requirements.txt # to install the exact version used in this project
```

## Building the Project

To test the project and build docs in one go in a *nix OS, you can use the `build.sh` script:

```
./build.sh
```

## License

This project is licensed under the "unlicense" terms of the included LICENSE file.

