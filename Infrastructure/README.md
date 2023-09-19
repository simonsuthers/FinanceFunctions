# Infrastructure as code
[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fsimonsuthers%2FFinanceFunctions%2Fmain%2FInfrastructure%2Fresource_group%2Fresource_group.json)

## Resource group
Connect to Azure with the following code:
```
Connect-AzAccount -TenantId 1708db9c-ec4d-4ad7-be06-f7fe5ce888b0
```

To deploy the resource group to Azure, run the following code:
```
New-AzSubscriptionDeployment `
  -Name ResourceGroupDeployment `
  -Location uksouth `
  -TemplateFile .resource_group/resource_group.json `
  -TemplateParameterFile .resource_group/resource_group.parameters.json
```


