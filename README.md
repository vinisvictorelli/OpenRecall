<p align="center">
  <img width="200" height="200" src="src/imgs/logo.png">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%20v3-yellow.svg" href="https://choosealicense.com/licenses/gpl-3.0/">
  <img src="https://img.shields.io/github/downloads/vinisvictorelli/OpenRecall/total" alt="Total Downloads">
</p>


<h2 align="left"> OpenRecall 📸 </h2>

OpenRecall is an attempt to recreate the features of Microsoft's Recall software. This tool creates a visual history of the user's activity and allows searching through this history using a description with the help of LLMs. The key difference is that OpenRecall runs entirely locally, unless the user wants, more about that later.

**DISCLAIMER: This tool is just a way I thought of to study more about the potential applications of LLMs in our daily lives. It is not recommended to use it as a backup solution for important information.**

## Features ✨

- **Automatic Screenshot Capture**: Takes screenshots by analyzing the pixels on the user's screen and saves them in a local folder (`capture` folder located at the project's root).
- **Image Description Generation**: Uses the **Minicpm-v** model to create detailed descriptions for each screenshot.
- **Efficient Search**: A search engine that quickly finds images and their descriptions based on your words.
- **Privacy**: All processing is done locally, with no need to send data to external servers.

### Next Steps
There is still room for several improvements, including:
- [ ] Running the entire application in a Docker container for easier execution.
- [ ] Improving the performance of image description, which is still **extremely slow.**
### Contributing

Feel free to open a pull request or report issues in the Issues section.
