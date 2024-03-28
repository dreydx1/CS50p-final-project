"""
MY SHORT SCRIPT FOR THE FINAL CS50P PROJECT
WITH THIS, YOU CAN GET THE CURRENT BASE GAS FEE IN GWEI FOR THE GIVEN CHAINS BELOW
PLEASE REFER TO THE README.md FILE FOR ANY INFORMATION
"""

import requests
import json
import sys
from dotenv import load_dotenv
import os

load_dotenv()


def main():
   selected_chain, API_URL = input_chain()
   gas_price_wei = get_gas_price(API_URL)
   print_gas_price(selected_chain, gas_price_wei)

def input_chain():

   API_KEY = os.getenv("API_KEY") # Not needed if you don't use dotenv
   if not API_KEY:
      print("API_KEY is NOT inside the environment.")
      sys.exit(1)

   chains = {
      # Paste your API key inside the curly brackets if you don't use dotenv
      # Here you can fetch other blockchains if you want to; just edit the dict
      
      "ETH": f"https://mainnet.infura.io/v3/{API_KEY}",
      "ARB": f"https://arbitrum-mainnet.infura.io/v3/{API_KEY}",
      "OP":  f"https://optimism-mainnet.infura.io/v3/{API_KEY}",
      "POLY": f"https://polygon-mainnet.infura.io/v3/{API_KEY}"
    }

   if len(sys.argv) != 2:
      print("No argument was given!")
      sys.exit(1)

   elif sys.argv[1] not in chains:
      print("Not a valid L1/L2 Chain!")
      sys.exit(1)

   selected_chain = sys.argv[1]
   API_URL = chains[selected_chain]

   return selected_chain, API_URL


def get_gas_price(API_URL):
   structure = {
      "jsonrpc": "2.0",
      "method": "eth_gasPrice",
      "params": [],
      "id": 1
   }

   headers = {"Content-Type": "application/json"}
   response = requests.post(API_URL, data=json.dumps(structure), headers=headers)

   if response.status_code == 200:
      result = response.json().get("result")
      return result
   else:
      print(f"Error fetching needed gas price: {response.text}")
      return None


def print_gas_price(selected_chain, gas_price_wei):
   gas_price_gwei = round(int(gas_price_wei, 16) / 1e9, 2) if gas_price_wei is not None else None
   print(f"{selected_chain} Gas Price:", gas_price_gwei, "GWEI ⛽️" if gas_price_gwei is not None else "")


if __name__ == "__main__":
   main()
