from project import input_chain
from project import get_gas_price
from project import print_gas_price
from project import main
from dotenv import load_dotenv
from unittest.mock import patch
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def test_main():
    with patch("requests.post") as mock_post, patch("builtins.print") as mock_print:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'result': '0x15f90'}
        with patch("sys.argv", ["test_get_gas.py", "ETH"]):
            main()
        mock_print.assert_called_with("ETH Gas Price:", 0, "GWEI ⛽️")

def test_input_chain():
    with patch("sys.argv", ["test_get_gas.py", "ETH"]):
        selected_chain, API_URL = input_chain()
        expected_chain = "ETH"
        expected_url = f"https://mainnet.infura.io/v3/{API_KEY}"
        assert selected_chain == expected_chain, f"Expected '{expected_chain}' but got {selected_chain}"
        assert API_URL == expected_url, f"Expected API_URL to be '{expected_url}', but got {API_URL}"

def test_get_gas_price():
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'result': '0x15f90'}
        gas_price = get_gas_price(f"https://mainnet.infura.io/v3/{API_KEY}")
        assert gas_price == "0x15f90", f"Expected '0x15f90', but got {gas_price}"

def test_print_gas_price():
    with patch("builtins.print") as mock_print:
        print_gas_price("ETH", "0x15f90")
        mock_print.assert_called_once_with("ETH Gas Price:", 0, "GWEI ⛽️")


if __name__ == "__main__":
    print("NICE JOB!")
    test_main()
    test_input_chain()
    test_get_gas_price()
    test_print_gas_price()
