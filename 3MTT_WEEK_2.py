{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPXKk8Z4dZvqzoIUSQDiuZd",
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
        "<a href=\"https://colab.research.google.com/github/Engrdutse/3MTT_DATA_SCIENCE/blob/main/3MTT_WEEK_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LiTRknOFgOA3",
        "outputId": "98afff62-3f75-4f39-ba6b-aca7bfe91663"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please select operation -\n",
            "1. Add\n",
            "2. Subtract\n",
            "3. Multiply\n",
            "4. Divide\n",
            "\n"
          ]
        }
      ],
      "source": [
        "#A program that will perfom simple Aljebraic Calculation\n",
        "\n",
        "\n",
        "# Function to add two numbers\n",
        "def add(num1, num2):\n",
        "    return num1 + num2\n",
        "\n",
        "# Function to subtract two numbers\n",
        "def subtract(num1, num2):\n",
        "    return num1 - num2\n",
        "\n",
        "# Function to multiply two numbers\n",
        "def multiply(num1, num2):\n",
        "    return num1 * num2\n",
        "\n",
        "# Function to divide two numbers\n",
        "def divide(num1, num2):\n",
        "    if num2 == 0:\n",
        "        return \"Error: Division by zero\"\n",
        "    else:\n",
        "        return num1 / num2\n",
        "\n",
        "print(\"Please select operation -\\n\" \\\n",
        "\t\t\"1. Add\\n\" \\\n",
        "\t\t\"2. Subtract\\n\" \\\n",
        "\t\t\"3. Multiply\\n\" \\\n",
        "\t\t\"4. Divide\\n\")\n",
        "\n",
        "\n",
        "# Take input from the user\n",
        "select = int(input(\"Select operations form 1, 2, 3, 4 :\"))\n",
        "\n",
        "number_1 = float(input(\"Enter first number: \"))\n",
        "number_2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "if select == 1:\n",
        "    print(number_1, \"+\", number_2, \"=\",\n",
        "                    add(number_1, number_2))\n",
        "\n",
        "elif select == 2:\n",
        "    print(number_1, \"-\", number_2, \"=\",\n",
        "                    subtract(number_1, number_2))\n",
        "\n",
        "elif select == 3:\n",
        "    print(number_1, \"*\", number_2, \"=\",\n",
        "                    multiply(number_1, number_2))\n",
        "\n",
        "elif select == 4:\n",
        "    print(number_1, \"/\", number_2, \"=\",\n",
        "                    divide(number_1, number_2))\n",
        "else:\n",
        "    print(\"Invalid input\")"
      ]
    }
  ]
}