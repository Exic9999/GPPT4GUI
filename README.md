## Overview

**YOU MUST HAVE ANACONDA INSTALLED TO RUN THIS CODE. Download the latest Anaconda and then install the libraries via the gpt_gui.yml into an environment of your choosing.**

The script creates a Graphical User Interface (GUI) desktop application that allows a user to interact with OpenAI's GPT-4 model (or any model you choose, you just need to edit the Python file, by default is GPT-4). Users can input text, which is sent to the GPT-4 model, and receive responses displayed in the application. 

## Libraries Used

- `tkinter`: A standard Python library for creating GUI applications.
- `openai`: The OpenAI library used to interact with the GPT-4 API.
- `threading`: A standard library for running processes in separate threads.

## Main Components

1. **Function: `send_request`**
   - Triggered when the user presses the Enter key or clicks the Send button.
   - It sends the user's input to the GPT-4 model and displays the response in the application.

2. **Threading**
   - The `api_call` function, which makes the call to the GPT-4 API, is run in a separate thread to prevent the GUI from freezing during the API call.

3. **OpenAI API Key**
   - The script requires an OpenAI API key to interact with the GPT-4 model. **Please enter in the script itself.**

4. **GUI Components**
   - The application window is created with Tkinter, consisting of input and output text boxes, a send button, and a loading label.

## Detailed Breakdown

1. **Creating the Main Window**
   - The script initializes a Tkinter window (`root`) with a specified size and background color.

2. **Defining Fonts**
   - Custom fonts for the input and output text areas.

3. **Input Frame**
   - A frame containing the user input box, the send button, and the loading label.

4. **User Input Box**
   - A scrolled text box where users can type their queries. It has a custom background color and font.

5. **Send Button**
   - When clicked, it triggers the `send_request` function. It changes color on hover for better user experience.

6. **Loading Label**
   - Displays a loading message while the API call is in progress.

7. **Output Box**
   - Displays the conversation history. It's read-only and scrolls automatically to show the latest messages.

8. **Event Loop**
   - The `mainloop` function keeps the application running and responsive to user interactions.

## Conclusion

This script creates a basic GUI using TKinter to use a ChatGPT API key as a desktop app, without relying on the on the web-based ChatGPT site.
