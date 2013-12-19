# script to generate the dataset as a CSV file

import pandas as p

data=p.read_csv("../inbox/comms-formation.csv", sep=",")

dataset = data[['ReceptionDate', '_RSSI', '_BOARD_TEMP', '_BYTES_RECEIVED', '_BYTES_SENT', '_NUMBER_OF_RESETS', '_VOLTAGE' ]]
dataset.to_csv('dataset.csv', ',')
