# Base Gas Fetcher
This small structured project fetches the current base gas fee for various Layer 1 Blockchains & Layer 2 scaling solutions for the Etherum blockchain.

This project does not fetch median and fast gas prices.
For estimated median and fast gas prices, please look more into gas oracles and other gas tracker.

>[!NOTE]
>The base gas fee is the minimum fee required to include a transaction in the next block, and it is determined by the network's congestion and demand for block space.

## Usage
Before you start to `git clone` this repository, you need to do the following three steps:

#### 1. Get an API key to access the data

- Paste your API key at the end of an endpoint (e.g. https://mainnet.infura.io/v3/{YOUR_API_KEY})
- I use Infura's API but it's possible to use other providers as well

#### 2. API environment variable

- You can paste your API key to .env but it's not a must
- I used the `dotenv` library for privacy reasons of course

#### 3. Run the code

- For it to work, a *command-line argument* is needed after "python project.py"
- The current four available options are: "ETH", "ARB", "OP", "POLY"

## Overview of the code

### project.py

- This file contains the "main" code of the project
- If you want to fetch other blockchains like AVAX or BSC, simply **edit** the dictionary inside `def input_chain()`
- It's also possbile to get the gas in WEI by adjusting the code inside the `def print_gas_price()` and `def main()` functions
- Overall, if you want to change soemthing in the code, this is where you should start

### test_project.py

- This is where all four functions of the project are tested
- Normally, your Python should come with the unittest.mock library pre-installed
- I've used the `unittest.mock` library together with the `patch()` decorator to test my functions
- I chose this lib because of the use of an API
- It mimics the behaviour of the API without actually sending any requests to our API
- Run `python test_project.py` inside your terminal to check if the code is actually working
    - If the tests were successful, you should get "NICE JOB!" printed to your terminal
- You can play around with the functions and/or create errors
- You can also run it with `pytest` to see if the tests were successful

## Installation
```
git clone https://github.com/dreydx1/

cd project

pip install -r requirements.txt

python project.py ETH
```
