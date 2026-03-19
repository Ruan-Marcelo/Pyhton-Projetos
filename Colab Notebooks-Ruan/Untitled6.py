{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 15532,
     "status": "ok",
     "timestamp": 1716487570772,
     "user": {
      "displayName": "ZRuanZito",
      "userId": "08939029772502865008"
     },
     "user_tz": 180
    },
    "id": "RUX9ACUbbn3L",
    "outputId": "efbb5caf-a066-43fb-857e-6da5dd8acf5b"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Insira o nome de uma fruta:             uva\n",
      "A fruta             uva não está presente na tupla.\n",
      "Insira o nome de uma fruta:                  uva\n",
      "A fruta uva não está presente na tupla.\n"
     ]
    }
   ],
   "source": [
    "# Exercicio 4\n",
    "\n",
    "listafrutas = (\"Banana\", \"Maçã\", \"Pera\", \"Uva\")\n",
    "\n",
    "fruta_emlista = input(\"Insira o nome de uma fruta: \")\n",
    "\n",
    "if fruta_emlista in listafrutas:\n",
    "    print(\"A fruta\", fruta_emlista, \"está presente na tupla.\")\n",
    "else:\n",
    "    print(\"A fruta\", fruta_emlista, \"não está presente na tupla.\")\n",
    "\n",
    "listafrutas = (\"Banana\", \"Maçã\", \"Pera\", \"Uva\")\n",
    "\n",
    "fruta_emlista = input(\"Insira o nome de uma fruta: \").strip().lower()\n",
    "\n",
    "if fruta_emlista in listafrutas:\n",
    "    print(\"A fruta\", fruta_emlista, \"está presente na tupla.\")\n",
    "else:\n",
    "    print(\"A fruta\", fruta_emlista, \"não está presente na tupla.\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyNqpAuuiNvXSKm0vSG9sYFI",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
