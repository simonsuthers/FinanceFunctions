# Visualising stock prices

[![Build and deploy Python project to Azure Function App](https://github.com/simonsuthers/FinanceFunctions/actions/workflows/release.yml/badge.svg)](https://github.com/simonsuthers/FinanceFunctions/actions/workflows/release.yml)

This project aims to collect and visualise stock prices. Stock prices are obtained from: https://www.alphavantage.co/documentation/

The project then aims to find correlations between prices and fundamentals.

## Basic overview of data lake
 - Azure function using http trigger loads pricing to data lake raw zone
 - Data is processed to process zone using Azure function and blob storage trigger
 - Data is served from process zone using Azure Synapse analytics server
  - API is created to get data from Azure Synapse server using Azure function
  - web app is created using React to visualise the data

## Key infrastructure steps
 - [x] Create resource group
 - [x] Create data lake with storage account using hot tier
 - [x] Create ARM template and deploy using PowerShell
 - [x] Add deploy to Azure button to Github
 - [x] Create Azure function with ARM template
    - [x] Create managed identity
    - [x] Give managed identity permissions to read/write to storage accounnt.
 - [x] Set up CI/CD for Azure function
 - [x] Create Key vault with ARM template
    - [x] Get function to call key vault
 - [x] Get function to save to blob storage
     - [x] Used managed identity permissions
 - [x] Get function to get data from alphavantage
      - [x] Save to blob storage
 - [x] Get function to save to blob storage using azure-storage-blob
 - [x] Add blueprint file
 - [ ] Add tests
 - [ ] Create function to save pricing by ticker to blob storage
 - [ ] Create list of master securities
 - [ ] Create logic app to run function app

Next steps:
Add tests:
https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators

## Log on to Azure with PowerShell
```
Connect-AzAccount
```

## Install frfom requirements.txt
```
pip install -r requirements.txt
```