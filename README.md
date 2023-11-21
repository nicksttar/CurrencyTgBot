# Currency Telegram Bot (AIogram 3)

This repository contains files to create a simple currency Telegram bot using AIogram 3 to handle interactions and requests for currency conversion.

## Description

The bot allows users to convert between different currencies by sending the bot a message in the format "amount currency/currency". For example: "USD/EUR" or "100 USD to EUR". The bot then queries the current exchange rate using an external API (for instance, Google Finance) and responds with the converted amount.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/CurrencyTgBot.git
    cd CurrencyTgBot
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Replace `<YOUR_API_KEY>` in `config.py` with your API key for accessing the currency conversion service.

4. Run the bot:

    ```bash
    python main.py
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
