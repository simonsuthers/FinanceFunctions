# Infrastructure as code

## Resource group
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsimonsuthers%2FFinanceFunctions%2Fmain%2FInfrastructure%2Fresource_group%2Fresource_group.json)

To deploy the resource group to Azure using PowerShell, run the following code:
```
New-AzSubscriptionDeployment `
  -Name ResourceGroupDeployment `
  -Location uksouth `
  -TemplateFile .resource_group/resource_group.json `
  -TemplateParameterFile .resource_group/resource_group.parameters.json
```


