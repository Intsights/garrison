<p align="center">
    <a href="https://github.com/intsights/garrison">
        <img src="https://raw.githubusercontent.com/intsights/garrison/master/images/logo.png" alt="Logo">
    </a>
    <h3 align="center">
        Queue server base on RocksDB as a KV-Store backend and gRPC as an interface
    </h3>
</p>

![license](https://img.shields.io/badge/MIT-License-blue)
![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8-blue)
![Build](https://github.com/intsights/garrison/workflows/Build/badge.svg)
[![PyPi](https://img.shields.io/pypi/v/garrison.svg)](https://pypi.org/project/garrison/)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Server](#server)
  - [Client](#client)
- [License](#license)
- [Contact](#contact)


## About The Project
Garrison is a RocksDB wrapped in a gRPC service to expose some high level functionalities.
Garrison is also implments queue functionalities on the top of RocksDB KV store functionalities.

### Built With
* [gRPC](https://grpc.io/)
* [RocksDB](https://rocksdb.org/)


### Prerequisites
In order to pip install rocksdb you will need to install the following distro packages

* Ubuntu 18.04
```sh
sudo apt install librocksdb-dev libsnappy-dev liblz4-dev
```

### Installation

```sh
pip3 install garrison-server
```



## Usage

### Server
```shell
python3 -m garrison.server --database-path=/data/garrison_db --port=10000
```

### Client
```python
import garrison.client

client = garrison.client.GarrisonClient(
    host='127.0.0.1',
    port=10000,
)

# Sets a key inside the database - return whether the key is new or existed
client.key_set(
    key=b'key_name',
    value=b'value',
)
# Retrieving a key - return None if key does not exist
value = client.key_get(
    key=b'key_name',
)
# Deletes a key inside the database - return whether the key is deleted or wasn't existed
deleted_successfuly = client.key_delete(
    key=b'key_name',
)


# Push items into a queue.
# Priority is either NORMAL or HIGH, and controls whether the items will be pushed on the top or buttom of the queue
client.queue_push(
    queue_name=b'queue_name',
    items=[
        b'item one',
        b'item two',
        b'item three',
    ],
    priority='NORMAL',
)
# Get the number of items in the queue
number_of_items = client.queue_length(
    queue_name=b'queue_name',
)
# Pulling items from the queue - return list of items. HIGH priority first.
items = client.queue_pop(
    queue_name=b'queue_name',
    number_of_items=3,
)
# Deletes a key inside the database - return whether the key is deleted or wasn't existed
deleted_successfuly = client.queue_delete(
    queue_name=b'queue_name',
)
```


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Gal Ben David - intsights@gmail.com

Project Link: [https://github.com/intsights/garrison](https://github.com/intsights/garrison)
