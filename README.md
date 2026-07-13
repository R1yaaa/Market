# Market

A stock-market simulation with a Qt-based GUI. Users can buy and sell rare goods, manage accounts and inventory, and watch prices fluctuate in real time.

The project is split into three layers:
- **C++ core** — market logic, accounts, goods, price generation
- **Python bridge** — pybind11 bindings + FastAPI REST server
- **Qt client** — GUI that communicates with the server via REST

---

## Project Structure

```
Market/
├── include/          # C++ header files
├── src/              # C++ source files (market logic)
├── extra/            # pybind11 bindings
├── tests/            # C++ unit tests (GTest)
├── examples/         # Usage examples
├── CMakeLists.txt    # C++ build configuration
├── requirements.txt  # Python dependencies
└── market.yaml       # Market configuration (goods, prices, etc.)
```

---

## Requirements

**C++:**
- CMake >= 3.12
- C++17 compiler (GCC, Clang, MSVC)
- pybind11
- Google Test (GTest)

**Python:**
- Python >= 3.10
- See `requirements.txt`

**Qt:**
- Qt 5 or Qt 6

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/R1yaaa/Market.git
cd Market
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Build the C++ library and Python bindings

```bash
mkdir build && cd build
cmake ..
make
```

This builds:
- `trading_lib` — the static C++ library
- `unolib` — the pybind11 Python module
- `run_tests` — the test executable

### 4. Copy the Python module

After building, copy `unolib*.so` (Linux/macOS) or `unolib*.pyd` (Windows) into the project root so Python can find it:

```bash
cp build/unolib*.so .   # Linux/macOS
```

---

## Running

### Start the REST server

```bash
uvicorn fastapi_server:app --reload
```

The server runs on `http://localhost:8000` by default.

### Start the Qt client

Open the Qt project and run it, or build it separately. It connects to the REST server automatically.

---

## Running Tests

### C++ unit tests

```bash
cd build
./run_tests
# or via CMake:
ctest
```

### Python tests

```bash
pytest
```

---

## Development

### Code style

```bash
black .        # auto-format Python
flake8 .       # lint Python
mypy .         # type check Python
```

### Adding a new good

Edit `market.yaml` and add a new entry under `goods`. The price generator will pick it up automatically on the next server start.

### Adding a new REST endpoint

Add the route in `fastapi_server.py` and call the corresponding pybind11 function from `unolib`.

---

## Architecture Overview

```
Qt Client  ←→  FastAPI REST Server  ←→  pybind11 (unolib)  ←→  C++ Core (trading_lib)
```

- The C++ core handles all market logic (buying, selling, price fluctuation)
- pybind11 exposes the C++ classes to Python
- FastAPI wraps them in a REST API
- The Qt client calls the REST API and displays the result
