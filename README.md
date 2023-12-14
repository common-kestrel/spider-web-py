# SpiderWeb 🕸

The SpiderWeb library is a custom Python data structure designed to organize elements in a hierarchical and indexed manner. It implements a linked structure with nodes organized in levels and indices. This library provides methods for adding, querying, and removing elements based on their levels and indices within the SpiderWeb.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
    - [SpiderWebNode](#spiderwebnode)
    - [SpiderWeb](#spiderweb)
3. [Examples](#examples)

## Installation

As of now, the SpiderWeb Python Library is not available on PyPI. You can include it in your project by following these steps:

1. Clone the repository or download the source code.
2. Manually add the library to your Python project.

```bash
# Example: Include SpiderWeb library locally
pip install /path/to/spiderweb
```

## Usage
### SpiderWebNode

The SpiderWebNode class represents a node in the SpiderWeb data structure.

```python
from spiderweb import SpiderWebNode

# Example Usage:
node = SpiderWebNode(53, None, None)

```
Attributes:
- value: The value stored in the node.
- prev_node: Reference to the previous node.
- prev_level_node: Reference to the node on the previous leve

### SpiderWeb

The SpiderWeb class is the main class for the SpiderWeb data structure.

```python
from spiderweb import SpiderWeb

# Example Usage:
spider_web = SpiderWeb()
spider_web.add(1)
spider_web.add(2)
spider_web.add(3)

```
Attributes:
- max_element_per_level: The maximum number of elements allowed per level (default is 6).

## Examples
### Creating a SpiderWeb Instance

```python
# Create a SpiderWeb instance with the default maximum elements per level (6)
spider_web = SpiderWeb()

# Create a SpiderWeb instance with a custom maximum elements per level (e.g., 8)
custom_spider_web = SpiderWeb(8)

```

### Adding Elements to the SpiderWeb

```python
# Add elements to the SpiderWeb
spider_web.add(42)
spider_web.add(56)
spider_web.add(78)

# Print the SpiderWeb contents
spider_web.print()

```

### Querying Elements in the SpiderWeb

```python
# Get the first and last elements in the SpiderWeb
first_element = spider_web.get_first()
last_element = spider_web.get_last()

# Get the size of the SpiderWeb
web_size = spider_web.size()

```

### Removing Elements from the SpiderWeb

```python
# Remove the first element and print the updated SpiderWeb
removed_element = spider_web.remove_first()
print("Removed element:", removed_element)

# Remove the last element and print the updated SpiderWeb
removed_element = spider_web.remove_last()
print("Removed element:", removed_element)

```

### Copying a SpiderWeb

```python
# Create a copy of the SpiderWeb
copied_web = spider_web.copy()

# Print the contents of the copied SpiderWeb
copied_web.print()

```

### Clearing the SpiderWeb

```python
# Clear all elements from the SpiderWeb
spider_web.clear()

# Print the SpiderWeb after clearing
spider_web.print()

```