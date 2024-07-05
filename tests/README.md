Banking Operations Widget Backend Server includes the following functional modules:

- decorators.py
- generators.py
- masks.py
- processing.py
- widget.py

### Functional Modules Overview:

#### decorators.py

Purpose:

- log(filename)
  - The log decorator is used for logging the results of a function execution.
  - Behavior:
    - If filename is provided, the result of the function execution will be written to the specified file.
    - If filename is not provided, the result of the function execution will be printed to the console.
  - Accepts an optional filename parameter (default **None**).
    - filename (str): The path to the file where logging will be performed.
  - Returns the wrapped function with logging.

#### generators.py

Purpose:
@@ -98,6 +112,7 @@ poetry install
The project testing is conducted using the tests package, which includes the following files:
- init.py
- conftest.py
- test_decorators.py
- test_generators.py
- test_masks.py
- test_processing.py