# PyMime: A Python Interface for Mimecast API

## Overview

PyMime is a Python-based interface designed to interact seamlessly with the Mimecast API. It simplifies the process of integrating Mimecast services into Python applications, offering a straightforward way to perform various operations like managing policies, handling directories, and authenticating requests.

## Features

- **Authentication Handling**: Automatically manages the authentication process using Mimecast API credentials.
- **Policy Management**: Facilitates operations related to policies, including retrieval and updates.
- **Directory Services**: Enables interactions with Mimecast's directory services, such as fetching profile groups and group members.
- **Test Suite**: Includes a comprehensive test suite for both unit testing and integration testing.

## Installation

To use PyMime in your project, clone this repository into your local workspace:

```bash
git clone https://github.com/your-github/PyMime.git
cd PyMime
```

(Optional) To run the project in a virtual environment, create one using your preferred method. For example, using `venv`:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before using PyMime, you need to set up your Mimecast API credentials. It is recommended to use environment variables for this purpose:

On Windows:

```cmd
set MIMECAST_CLIENT_ID=your_client_id
set MIMECAST_CLIENT_SECRET=your_client_secret
```

On Linux or macOS:

```bash
export MIMECAST_CLIENT_ID=your_client_id
export MIMECAST_CLIENT_SECRET=your_client_secret
```

## Usage

Import `PyMime` from the package and initialize it with your credentials:

```python
from pymime import PyMime

mimecast = PyMime(client_id="your_client_id", client_secret="your_client_secret")
```

### Example Operations

- **Get Policies**:

  ```python
  policies = mimecast.get_policies()
  print(policies)
  ```

- **Get Group Members**:

  ```python
  group_members = mimecast.get_group_members(group_id="group_id_here")
  print(group_members)
  ```

## Testing

PyMime comes with a suite of tests. To run them:

```bash
pytest
```

For verbose output, use:

```bash
pytest -v
```

## Contributing

Contributions to PyMime are welcome! Please follow the usual fork-and-pull-request workflow. Make sure to add/update tests as necessary.