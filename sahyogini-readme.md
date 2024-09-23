# Sahyogini: AI-Powered Chatbot for Women Empowerment

Sahyogini is an AI-powered chatbot designed to guide underprivileged women through relevant government schemes in India. Hosted on Telegram, it provides personalized responses based on user profiles, with future plans to support voice-based interactions.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- AI-powered responses using GPT-based models
- Personalized scheme recommendations based on user profiles
- Integration with Telegram for easy access
- Web scraping of government websites for up-to-date scheme information
- Knowledge graph for efficient information storage and retrieval
- Data privacy and management system

## Technology Stack

- Python 3.8+
- Rasa for chatbot framework
- Neo4j for knowledge graph
- OpenAI GPT for natural language processing
- BeautifulSoup and Scrapy for web scraping
- Telegram Bot API for messaging interface

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/sahyogini.git
   cd sahyogini
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_api_key
   NEO4J_URI=your_neo4j_uri
   NEO4J_USER=your_neo4j_username
   NEO4J_PASSWORD=your_neo4j_password
   ```

5. Set up the Neo4j database:
   - Install Neo4j and create a new database
   - Run the setup scripts in `database_setup/` to initialize the knowledge graph

6. Train the Rasa model:
   ```
   rasa train
   ```

## Usage

1. Start the main application:
   ```
   python main.py
   ```

2. The Telegram bot will start running. Users can interact with it by searching for the bot on Telegram and starting a conversation.

3. To update the knowledge graph with new scheme information, run:
   ```
   python update_schemes.py
   ```

## Project Structure

- `main.py`: Entry point of the application
- `scraper.py`: Web scraping module
- `knowledge_graph.py`: Neo4j knowledge graph interface
- `llm_interface.py`: Interface with the GPT-based model
- `chatbot.py`: Rasa chatbot implementation
- `telegram_bot.py`: Telegram bot integration
- `data_manager.py`: Data management and privacy handling
- `config.py`: Configuration settings
- `database_setup/`: Scripts for setting up the Neo4j database
- `rasa/`: Rasa training data and configuration files

## Contributing

We welcome contributions to Sahyogini! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Team:
- Ritika Chhabra - ritika.madaan01@gmail.com
- Varisha Garg - er.singla.varisha@gmail.com
- Richa Gupta - richagwork@gmail.com

Project Link: [https://github.com/your-username/sahyogini](https://github.com/your-username/sahyogini)

---

Sahyogini is committed to empowering women through simplified access to government schemes. We believe in the power of technology to bridge information gaps and create positive social impact.
