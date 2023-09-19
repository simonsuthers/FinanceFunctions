# Infrastructure as code

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


New-AzResourceGroupDeployment -Name ResourceGroupDeployment -ResourceGroupName ExampleResourceGroup `
  -TemplateFile <path-to-template> `
  -TemplateParameterFile c:\MyTemplates\storage.parameters.json
```


