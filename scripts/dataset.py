# script to generate the dataset as a CSV file

import pandas as p

data=p.read_csv("../inbox/comms-formation.csv", sep=",")

dataset = data[['ReceptionDate', '_RSSI', '_BOARD_TEMP']]
dataset.to_csv('dataset.csv', ',')
