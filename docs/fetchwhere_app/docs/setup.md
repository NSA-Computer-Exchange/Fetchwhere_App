# Fetchwhere App

## Commands

* The simplest way to get started is to clone this repository to a local directory.
* `git clone https://github.com/NSA-Computer-Exchange/Fetchwhere_App`

## Download

If you don't have git installed, you can download the files in .zip format:

* Expand the green "Code" button.
* Select __Download ZIP__ at the bottom.

![Download](img/download.jpg)

For more information on cloning a repository, here's a good read: [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Config
You'll need to edit the __config.ini__ file so it points to your __tenant__ and your __.ionapi__ credential file.

    config/
        config.ini  

__Edit this line:__
    
    conoFetchUrl = https://mingle-ionapi.inforcloudsuite.com/TENANT_TRN/SX/rest/serviceinterface/proxy/FetchWhere   

Replace the __TENANT_TRN__ value in the Fetchwhere URL with your tenant.  

__Example:__ 
    
    https://mingle-ionapi.inforcloudsuite.com/ACMECORP_TRN/SX/rest/serviceinterface/proxy/FetchWhere


From yor InforOS tenant, create a backend service and downlod the __.ionapi__ credential file.  
Save the __.ionapi__ file in the __config__ folder. 
You can name it anything you like and even save it anywhere you want but you will have to change the path and name in the __config.ini__ file to point to the correct location and file.

    config/
        mycredentials.ionapi

__Edit__ this line to point to your file.

    ionapi_file = ./config/mycredentials.ionapi

## Editing the payload

You'll find the various payloads in the payloads folder.
They are just examples that you can use or modify freely to suite your needs.

    payloads/
        sasc.json
        sasoo.json
        sasp.json
        vaeh.json

__Example:__ SASOO request

    {  
        "CompanyNumber": 1000,
        "Operator": "sys",
        "TableName": "sasoo",
        "WhereClause": "cono = 1000 and oper2 = 'RT01'",
        "BatchSize": 0,
        "RestartRowID": "" 
    }

Once you have the repository cloned or downloaded and your payload(s) setup,
 __make sure__ you have adequate permissions on the root directory the code is installed in and proceed to [Running the code](running.md) 