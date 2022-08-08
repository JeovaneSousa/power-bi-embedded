# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '41e24042-2290-43b0-a018-961532445d7f'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '1758b7f7-801c-4de2-bdba-3501de850fdc'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = 'aff42214-80c9-4cfa-aa6f-3ed338112ff6'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '5d08a95d-2b70-4663-ae1d-2b1f2a7a304d'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'ziM8Q~8ODe7DIpgZxW4Gxqj7JyF6DQ3cYbCjdc0.'

    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''