# Visualising stock prices

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
    - [ ] Create managed identity
    - [ ] Give managed identity permissions to read/write to storage accounnt.
 - [ ] Set up CI/CD for Azure function
 - [ ] Create Key vault with ARM template
 - [ ] Change function to API style with swagger ui

Next steps:
Adding Azure storage:
https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?pivots=programming-language-python&tabs=in-process%2Cv1