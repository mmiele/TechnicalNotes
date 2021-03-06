# Bot Framework v4 Conversation Bot sample for Teams

This article shows how to incorporate a conversational bot into [Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software). You will learn the following:

1. Deploy the conversation bot to Azure.
1. Test the bot running on your local machine using the Bot Emulator.
1. Test the bot running on your local machine using Teams.
1. In Teams, use the bot running in Azure. 

The article uses the example code on GitHub found at this location: [conversation bot](https://github.com/microsoft/BotBuilder-Samples/tree/master/samples/python/57.teams-conversation-bot).

The bot has been created using [Bot Framework v4](https://dev.botframework.com). 

## Prerequisites

- Microsoft Teams is installed and you have an account
- [Python SDK](https://www.python.org/downloads/) min version 3.6
- [ngrok](https://ngrok.com/) or equivalent tunnelling solution
- [Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator/blob/master/README.md)


## Deploy the bot to Azure preliminary steps

1. Clone the latest bot builder samples:

    ```bash
    git clone https://github.com/Microsoft/botbuilder-samples.git
    ```

1. Open a terminal window and change directory to `..BotBuilder-Samples\samples\python\57.teams-conversation-bot`.
1. Execute the following commands: 

    ```bash
        pip install azure-storage-blob>=2.1.0 # do we need this?
    ```

    Install dependencies.

    ```bash
        pip install -r requirements.txt
    ```

 1. Deploy the bot to Azure using the latest [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest). For more information, see [Tutorial: Create and deploy a basic bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-basic-deploy?view=azure-bot-service-4.0&tabs=csharp). The following is an example of the steps to follow:

    1. Login into Azure

        ``` cmd
        az login
        ```

    1. Set the subscription

        ```cmd
        az account set --subscription "<<your subscription>>"
        ```

    1. Set Azure Active Directory Graph entities needed for Role Based Access. This step also produces the **app id** to use in the next step.

        ```cmd
        az ad app create --display-name "TeamsConversation" --password "<<your password>>" --available-to-other-tenants
        ```

    1. Start deployment via ARM template. This step also produces the subscription id to use in the next step.
    
        ```cmd
        az deployment create --name "TeamsConversation" --template-file "..BotBuilder-Samples\samples\python\57.teams-conversation-bot\deploymentTemplates\template-with-new-rg.json" --location "westus" --parameters appId="<<get it from previous step>>" appSecret="<<your password>>" botId="TeamsConversation" botSku=F0 newAppServicePlanName="<<your plan name>>" newWebAppName="TeamsConversation" groupName="<<your group name>>" groupLocation="westus" newAppServicePlanLocation="westus"
        ```

    1. Optionally, check App Id and Password settings

        ```cmd
        az webapp config appsettings list -g mm-python-group -n TeamsConversationNew --subscription  <<your subscription id>>
        ```

    You can run the az cli commands from within Visual Studio Code using the [AZ CLI extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azurecli).  See also [The Azure Command-Line Interface (CLI)](https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest).

## Test the bot using the Bot Emulator

Before deploying the bot to Azure let's test it on the local machine.

1. In a terminal window, navigate to `..BotBuilder-Samples\samples\python\57.teams-conversation-bot`.
1. Execute this command:

    ```cmd
    python app.py
    ```

    The following message is displayed:

    ![teams conversation app emulator](../Media/Python/teams-conversation-app-emulator.PNG)

1. Open a new terminal window and execute this command:

    ```cmd
    ngrok http -host-header=rewrite 3978
    ```

    You get the following output:

    ![teams conversation app ngrok](../Media/Python/teams-conversation-app-ngrok.PNG) 

1. Copy the **https forwarding** address which is similar to this: `https://e075240a.ngrok.io`. 
1. Copy the address to a file and add to it `api/messages`, so the address is similar to this `https://e075240a.ngrok.io/api/messages`.
   This the **end point** to connect with the bot running locally.
1. Activate the Bot Framework Emulator. 
1. Click the **Open Bot** button.
1. In the **Bot URL** box, enter the end point address you saved before such as `https://e075240a.ngrok.io/api/messages`. 
1. In the **Microsoft App ID** box enter the same app id value you entered earlier in `config.py` and `manifest.json`.  
1. In the **Microsoft App  password** box enter the same password value you entered earlier in `config.py`.
    > NOTE
    > If you restart ngrok, the end point URL changes and you must restart the emulator and enter the new URL.
1. Click the **Connect** button.
1. Wait for the emulator to connect to the bot. You should see a *201 Created* message in the ngrok terminal window,
1. Enter any text in the emulator box, for example *hello*.
1. The welcome card is displayed. This means that the bot is working correctly.

    ![teams conversation app emulator welcome card](../Media/Python/teams-conversation-app-emulator-welcome-card.PNG) 

## Deploy the bot to Azure final steps

 1. Before performing the deployment step, you must prepare the bot code as described below.

    1. Create `manifest.zip` file
        1. Navigate to `BotBuilder-Samples\samples\python\57.teams-conversation-bot\teams_app_manifest` directory.
        1. In your editor, open the `manifest.json` file.  Assign the `id` and `bot Id` variables assign the **app id** obtained before.
        1. Save the file.
        1. Select all the files in the directory and zipped them up in a file such as `manifest.zip`.

    1. Create `app.zip` file
        1. Navigate to `BotBuilder-Samples\samples\python\57.teams-conversation-bot` directory.
        1. In your editor, open the `config.py` file.  Assign the **app Id** and the **password** values from the previous step.
        1. Save the file.
        1. Select all the files in the directory and zipped them up in a file such as `app.zip`.

    1. Deploy the bot

        ```cmd
        az webapp deployment source config-zip --resource-group "mm-python-group" --name "TeamsConversation" --src "..BotBuilder-Samples\samples\python\57.teams-conversation-bot\app.zip"
        ```

        if you navigate to the Azure portal, you should see the bot app registration and app service listed as shown below. 
        ![teams conversation bot deployed](../Media/Python/teams-conversation-bot-deployed.PNG).

At this point the bot is ready to be used from within Teams.

## Using the bot within Teams

1. Activate your Microsoft Teams.
1. In the lower left, left panel, click the **Apps** icon.
1. In the right panel, click the **Upload a custom app** link.
1. Navigate to the directory `..BotBuilder-Samples\samples\python\57.teams-conversation-bot\teams_app_manifest`.
1. Select the `manifest.zip` file.
1. Click the **Open** button.
1. In the Teams wizard window, click the arrow in the **Add** button and select *Add to a team* or *Add to a chat*.

    ![teams conversation bot wizard](../Media/Python/teams-conversation-bot-wizard.PNG) 

1. In the next window, select the team or chat where to add the bot.
1. Click the **Setup a bot** button.
1. After the bot is set, you can start entering the allowed requests 
1. If you enter *Show Welcome*, the welcome card is displayed. This means that the bot is working correctly and can be used within Teams.

     ![teams conversation bot welcome card](../Media/Python/teams-conversation-bot-welcome-card.PNG) 

You can interact with the bot by sending it a message, or selecting a command from the command list. The bot will respond to the following strings.

|Personal|Group|Team|Result|
|:---|:---|:---|:---|
|Show Welcome<br/>Mention Me<br/>Message All Members|Show Welcome<br/>Mention Me<br/>Message All Members|Show Welcome<br/>Mention Me<br/>Message All Members|Welcome card for you to interact with<br/>Mention the user<br/>1-on-1 message to each member in the current conversation|
