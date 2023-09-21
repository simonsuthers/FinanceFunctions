# Infrastructure as code

## Resource group
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsimonsuthers%2FFinanceFunctions%2Fmain%2FInfrastructure%2Fresource_group%2Fresource_group.json)

## Storage

```
$url = "https://raw.githubusercontent.com/simonsuthers/FinanceFunctions/main/Infrastructure/storage/storage.json"
[uri]::EscapeDataString($url)
```

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsimonsuthers%2FFinanceFunctions%2Fmain%2FInfrastructure%2Fstorage%2Fstorage.json)


To deploy the resource group to Azure using PowerShell, run the following code:
```
cd C:\Users\simon\hello\Infrastructure\
New-AzResourceGroupDeployment -ResourceGroupName rg-ss-financeapp-001 -TemplateFile storage/storage.json
```

## Key Vault 
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsimonsuthers%2FFinanceFunctions%2Fmain%2FInfrastructure%2Fkeyvault%2Fkeyvault.json)

## Function 
### App plan
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsimonsuthers%2FFinanceFunctions%2Fmain%2FInfrastructure%2Ffunction%2Fapp_plan.json)

### Finance function
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsimonsuthers%2FFinanceFunctions%2Fmain%2FInfrastructure%2Ffunction%2Ffinance_function.json)




