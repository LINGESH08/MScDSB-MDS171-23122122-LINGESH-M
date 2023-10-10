{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMoQsjIdWWf/8SiRMnETc5s",
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
        "<a href=\"https://colab.research.google.com/github/LINGESH08/MScDSB-MDS171-23122122-LINGESH-M/blob/main/Lab_09.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\" Create a petstore class where you have the details of pets available and their details.\n",
        "\n",
        "The class will have methods\n",
        "\n",
        "- Store a new pet details\n",
        "- Search for a pet\n",
        "- Sell a pet\n",
        "- List all pets\n",
        "\n",
        "importing your petstore class, create a petstoremain file, where you will implement a menu driven program for Admin -\n",
        "who will manage the store and User who will see the pets and buy pets. \"\"\""
      ],
      "metadata": {
        "id": "qHP_uzar5btt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"class petStore\n",
        "      def __init__(self):\n",
        "        self.pets = {\n",
        "          \"dogs\" : [],\n",
        "          \"cat\" : [],\n",
        "          \"rabbit\" : [],\n",
        "          \"parrot\" : []\n",
        "        }\n",
        "      def collectPet(self,....)\n",
        "          pass\"\"\""
      ],
      "metadata": {
        "id": "xR3khD0xqUV2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class petStore:\n",
        "  def __init__(self):\n",
        "    self.pets = {\n",
        "        \"dogs\" : [],\n",
        "        \"cats\" : [],\n",
        "        \"rabbits\" : [],\n",
        "        \"parrots\" : []\n",
        "    }\n",
        "  def storePet(self, type, breedName, price, age):\n",
        "    temp = {\n",
        "        \"breedName\" : breedName,\n",
        "        \"price\" : price,\n",
        "        \"age\" : age\n",
        "    }\n",
        "    self.pets[type].append(temp)"
      ],
      "metadata": {
        "id": "Eobt8Zee6tNQ"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pets = petStore()\n",
        "print(pets.pets)\n",
        "pets.storePet('dogs', 'Juju', 12000,21)\n",
        "print(pets.pets)\n",
        "pets.storePet('dogs', 'Kutha', 1000,22)\n",
        "print(pets.pets)\n",
        "pets.storePet('cats', 'Meow', 500,23)\n",
        "print(pets.pets)\n",
        "pets.storePet('rabbits', 'Looni', 20000,24)\n",
        "print(pets.pets)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TNLArFDa3N5D",
        "outputId": "b161401f-8e68-4628-8595-84fb3fee09ce"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'dogs': [], 'cats': [], 'rabbits': [], 'parrots': []}\n",
            "{'dogs': [{'breedName': 'Juju', 'price': 12000, 'age': 21}], 'cats': [], 'rabbits': [], 'parrots': []}\n",
            "{'dogs': [{'breedName': 'Juju', 'price': 12000, 'age': 21}, {'breedName': 'Kutha', 'price': 1000, 'age': 22}], 'cats': [], 'rabbits': [], 'parrots': []}\n",
            "{'dogs': [{'breedName': 'Juju', 'price': 12000, 'age': 21}, {'breedName': 'Kutha', 'price': 1000, 'age': 22}], 'cats': [{'breedName': 'Meow', 'price': 500, 'age': 23}], 'rabbits': [], 'parrots': []}\n",
            "{'dogs': [{'breedName': 'Juju', 'price': 12000, 'age': 21}, {'breedName': 'Kutha', 'price': 1000, 'age': 22}], 'cats': [{'breedName': 'Meow', 'price': 500, 'age': 23}], 'rabbits': [{'breedName': 'Looni', 'price': 20000, 'age': 24}], 'parrots': []}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "3z-76KX73zTR"
      },
      "execution_count": 7,
      "outputs": []
    }
  ]
}