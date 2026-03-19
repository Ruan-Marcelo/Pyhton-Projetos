{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 356
    },
    "executionInfo": {
     "elapsed": 868,
     "status": "error",
     "timestamp": 1725461184195,
     "user": {
      "displayName": "ZRuanZito",
      "userId": "08939029772502865008"
     },
     "user_tz": 180
    },
    "id": "-Jm2Jp_yf-fk",
    "outputId": "1ab4f524-49e8-4eda-d3dc-24e6916c545b"
   },
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "from turtle import *\n",
    "\n",
    "def hearta(R):\n",
    "    return 12*math.sin(R)**3\n",
    "def heartb(R):\n",
    "    return 12*math.cos(R)-5*\\\n",
    "    math.cos(2*R)-2*\\\n",
    "                math.cos(3*R)-\\\n",
    "                math.cos(4*R)\n",
    "speed(0)\n",
    "bgcolor(\"black\")\n",
    "for i in range(10000):\n",
    "    goto(hearta(i)*20, heartb(i)*2)\n",
    "    for j in range(5):\n",
    "        color(\"#f73487\")\n",
    "        goto(0,0)\n",
    "done()"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyNnWyI+TrIMTH4R6xQNkIZ4",
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
