# Chainlit-Phidata Health and Fitness Assistant

This project demonstrates an integration between Chainlit and phidata, leveraging the Claude AI model to create an interactive chat interface focused on health and fitness guidance.

## Features

- Real-time AI responses using Claude 3 Sonnet
- Seamless integration of Chainlit's UI with phidata's assistant capabilities
- Streaming responses for a smooth user experience
- Specialized knowledge in health and fitness topics

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- Anthropic API key

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/waveup/chainlit-phidata-health-assistant.git
   cd chainlit-phidata-health-assistant
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

4. Create a `.env` file in the project root and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Chainlit application:

   ```
   chainlit run app.py -w
   ```

2. Open your web browser and navigate to `http://localhost:8000` (or the URL provided in the terminal).

3. Start chatting with the AI assistant about your health and fitness questions!

## Project Structure

- `app.py`: Main application file containing the Chainlit-phidata integration code
- `phidata_assistant.py`: Contains the AssistantInterface class and initialization
- `chainlit.md`: Markdown file for the Chainlit landing page
- `requirements.txt`: List of Python dependencies
- `README.md`: This file, containing project information and instructions

## Example Topics

The Health and Fitness Assistant can help with various topics, including:

- Workout routines
- Nutrition advice
- Weight management
- Fitness goal setting
- General health questions

Remember, while this AI can provide general advice, it's always best to consult with healthcare professionals for personalized medical guidance.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Chainlit](https://github.com/Chainlit/chainlit) for the chat interface
- [phidata](https://github.com/phidatahq/phidata) for the AI assistant framework
- [Anthropic](https://www.anthropic.com) for the Claude AI model
