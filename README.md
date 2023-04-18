# Mac-RAM-Cleaner
# Mac RAM Cleaner

Mac RAM Cleaner is a simple Python script that helps you clean your MacBook Pro M1's memory, improving system performance. It displays memory usage details, clears cache files, and provides an easy way to monitor and manage your Mac's memory usage.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Requirements

- macOS with an M1 chip
- Python 3.7 or later

## Installation

1. Clone the repository or download the source code:

https://github.com/Dimon1011/Mac-RAM-Cleaner/


2. Navigate to the project directory:

cd Mac-RAM-Cleaner


## Usage

1. Open Terminal and navigate to the project directory.

2. Run the script using the following command:

python3 clean_ram.py -c


This command will display memory usage details, clear the cache, and show the updated memory usage.

3. If you want to display memory usage without clearing the cache, run the script without the `-c` option:

python3 clean_ram.py


Please note that macOS manages memory efficiently, and you may not see significant changes in memory usage after running the script. However, it can still help improve performance by removing cached files that are no longer needed.

## License

[MIT License](LICENSE)

