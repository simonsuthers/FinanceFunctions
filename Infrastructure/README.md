# Infrastructure as code

## Resource group
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsimonsuthers%2FFinanceFunctions%2Fmain%2FInfrastructure%2Fresource_group%2Fresource_group.json)

## Storage

```
$url = "https://github.com/simonsuthers/FinanceFunctions/blob/main/Infrastructure/storage/storage.json"
[uri]::EscapeDataString($url)
```

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fgithub.com%2Fsimonsuthers%2FFinanceFunctions%2Fblob%2Fmain%2FInfrastructure%2Fstorage%2Fstorage.json)


To deploy the resource group to Azure using PowerShell, run the following code:
```
New-AzResourceGroupDeployment -ResourceGroupName rg-ss-financeapp-001 -TemplateFile .storage/storage.json

New-AzSubscriptionDeployment `
  -Name ResourceGroupDeployment `
  -Location uksouth `
  -TemplateFile .resource_group/resource_group.json `
  -TemplateParameterFile .resource_group/resource_group.parameters.json
```


