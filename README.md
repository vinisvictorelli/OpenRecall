# Freecall

Freecall is an attempt to recreate the features of Microsoft's Recall software. This tool creates a visual history of the user's activity and allows searching through this history using a description provided by the user with the help of LLMs. The key difference is that Freecall runs entirely locally, eliminating the risk of sending your information to external servers.

**DISCLAIMER: This tool is just a way I thought of to study more about the potential applications of LLMs in our daily lives. It is not recommended to use it as a backup solution for important information.**

## Features

- **Automatic Screenshot Capture**: Takes screenshots by analyzing the pixels on the user's screen and saves them in a local folder (`capture` folder located at the project's root).
- **Image Description Generation**: Uses the **Minicpm-v** model to create detailed descriptions for each screenshot.
- **Efficient Search**: A search engine that quickly finds images and their descriptions based on your words.
- **Privacy**: All processing is done locally, with no need to send data to external servers.

## How to Use

### 1. Capture Screenshots
Click on "Capture Screen" to start taking screenshots automatically. These will be saved in the `capture` folder within the application's directory.

### 2. Describe Images
After capturing screenshots, click on "Describe Images" to process and generate descriptions for them using the **Minicpm-v** model.

### 3. Search History
Use the built-in search engine to find previous images and information using your own words.

## Running the Project

### 1. Prerequisites

- **Python 3.12** or higher.
- **Ollama** to manage the **Minicpm-v** model.
- **Streamlit** to run the web application.

### 2. Installing Dependencies

Clone the repository and install the project dependencies.

```bash
git clone https://github.com/usuario/freecall.git
cd freecall
pip install -r requirements.txt
```
### 3. Setting Up Ollama

Make sure Ollama is properly installed. If not, you can install it using the command below:

```bash
curl -sSfL https://ollama.com/download.sh | sh
```

After installing Ollama, download the Minicpm-v model:

```bash
ollama pull minicpm-v
```

### 4. Running the Application

Run the application using Streamlit:
```bash
streamlit run app.py
```

### Next Steps
There is still room for several improvements, including:
- [ ] Running the entire application in a Docker container for easier execution.
- [ ] Improving the performance of image description, which is still **extremely slow.**
### Contributing

Feel free to open a pull request or report issues in the Issues section.
