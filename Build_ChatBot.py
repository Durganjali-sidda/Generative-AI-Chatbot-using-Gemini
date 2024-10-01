{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNP7aAuMW74Z41aKjlNoTQZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Durganjali-sidda/Generative-AI-Chatbot-using-Gemini/blob/main/Build_ChatBot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "E4l8Ndif1zPk"
      },
      "outputs": [],
      "source": [
        "import google.generativeai as genai\n",
        "import os\n",
        "import time\n",
        "\n",
        "os.environ[\"API_KEY\"] = \"AIzaSyAMOnki4YtNzkcsigs2R-lvZsOnsCN1lSE\"  # Your API key\n",
        "genai.configure(api_key=os.environ[\"API_KEY\"])\n",
        "\n",
        "model = genai.GenerativeModel('gemini-1.5-pro-latest')\n",
        "\n",
        "user_name = None  # Store user's name\n",
        "\n",
        "def chat_with_bot(prompt):\n",
        "    \"\"\"\n",
        "    Chats with a Google Generative AI model.\n",
        "    Includes features like personalization, typing indicator,\n",
        "    error handling, and raising exceptions.\n",
        "\n",
        "    Args:\n",
        "        prompt: The user's input prompt.\n",
        "\n",
        "    Returns:\n",
        "        The bot's response.\n",
        "\n",
        "    Raises:\n",
        "        genai.errors.APIError: If there's an issue with the API.\n",
        "        genai.errors.AuthenticationError: If authentication fails.\n",
        "        genai.errors.ResourceExhaustedError: If resources are exhausted.\n",
        "        Exception: For any other unexpected errors.\n",
        "    \"\"\"\n",
        "    global user_name\n",
        "    try:\n",
        "        # Get user's name if not already known\n",
        "        if user_name is None:\n",
        "            user_name = input(\"What's your name? \")\n",
        "            return f\"Hello {user_name}, nice to meet you! How can I help you today?\"\n",
        "\n",
        "        # Handle basic questions with predefined responses\n",
        "        if prompt.lower() in [\"hi\", \"hello\", \"hey\"]:\n",
        "            return f\"Hello {user_name}!\"\n",
        "        elif prompt.lower() == \"how are you?\":\n",
        "            return f\"I'm doing well, thank you, {user_name}!\"\n",
        "        elif prompt.lower() == \"what's your name?\":\n",
        "            return \"I'm a Google Generative AI model.\"\n",
        "\n",
        "        # Simulate typing indicator\n",
        "        print(\"Bot is typing...\", end=\"\", flush=True)\n",
        "        time.sleep(1)  # Adjust delay as needed\n",
        "        print(\"\\r\", end=\"\", flush=True)  # Clear typing indicator\n",
        "\n",
        "        # Generate a response from the model\n",
        "        response = model.generate_content(prompt)\n",
        "        return response.text\n",
        "\n",
        "    except genai.errors.APIError as e:\n",
        "        raise  # Re-raise the APIError\n",
        "    except genai.errors.AuthenticationError as e:\n",
        "        raise  # Re-raise the AuthenticationError\n",
        "    except genai.errors.ResourceExhaustedError as e:\n",
        "        raise  # Re-raise the ResourceExhaustedError\n",
        "    except Exception as e:\n",
        "        raise  # Re-raise any other exception\n",
        "\n",
        "# Example usage:\n",
        "print(\"Welcome to the chatbot! Type 'exit' to quit.\")\n",
        "while True:\n",
        "    user_input = input(\"You: \")\n",
        "    if user_input.lower() == \"exit\":\n",
        "        print(\"Exiting chat. Goodbye!\")\n",
        "        break\n",
        "    try:\n",
        "        response = chat_with_bot(user_input)\n",
        "        print(\"Bot:\", response)\n",
        "    except Exception as e:\n",
        "        print(f\"An error occurred: {type(e).__name__}: {e}\")"
      ]
    }
  ]
}