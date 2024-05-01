```markdown
# Bitcoin Block Alert

## Introduction
The Bitcoin Block Alert script is designed to monitor the Bitcoin blockchain and alert users when a specific block height is reached. This tool is particularly useful for those who want to track milestones in the Bitcoin network, such as halving events or other significant block heights.

## Features
- Fetches the current Bitcoin block height using the Blockchain.info API.
- Allows users to set a target block height and receive desktop notifications when this height is reached.
- Runs continuously, checking the blockchain at regular intervals.

## Requirements
- Python 3.x
- Requests library
- MacOS (due to the use of AppleScript for notifications)

## Installation

### Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/bitcoin-block-alert.git
cd bitcoin-block-alert
```

### Install Dependencies
Install the required Python libraries using pip:

```bash
pip install requests
```

## Usage
To use the script, navigate to the script directory and run:

```bash
python bitcoin_block_alert.py
```

Follow the on-screen prompts to enter the target block height you are interested in monitoring.

## Contributing
Contributions to the Bitcoin Block Alert project are welcome! Please feel free to fork the repository, make changes, and submit pull requests. You can also open issues if you find bugs or have feature suggestions.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Contact
For any additional questions or feedback, please contact [red.chiang@gmail.com](mailto:red.chiang@gmail.com).

```
