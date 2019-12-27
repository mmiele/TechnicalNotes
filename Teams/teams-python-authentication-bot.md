# Bot Framework v4 Authentication Bot sample for Teams

This article shows how to incorporate an authentication bot into [Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software). You will learn the following:

1. Deploy the Authentication bot to Azure.
1. Test the bot running on your local machine using the Bot Emulator.
1. Test the bot running on your local machine using Teams.
1. In Teams, use the bot running in Azure.

The article uses the example code on GitHub found at this location: [teams authentication bot](https://github.com/microsoft/BotBuilder-Samples/tree/master/samples/python/46.teams-auth).

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

1. Open a terminal window and change directory to `*\BotBuilder-Samples\samples\python\46.teams-auth`.
1. Make sure that the `requirements.txt` file contains the following dependencies

    ```text
    aiohttp
    botbuilder-core>=4.7.0
    botbuilder-dialogs>=4.7.0 
    ```

    Install the dependencies.

    ```cmd
    pip install -r requirements.txt
    ```

 1. Deploy the bot to Azure using the latest [Azure Command-Line Interface (CLI)](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest). For more information, see [Tutorial: Create and deploy a basic bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-basic-deploy?view=azure-bot-service-4.0&tabs=csharp). The following is an example of the steps to follow:

    1. Login into Azure

        ``` cmd
        az login
        ```

    1. Set the subscription

        ```cmd
        az account set --subscription "<<your subscription>>"
        ```

        If you are not sure which subscription to use for deploying the bot, you can view the list of subscriptions for your account by using the `az account list` command.

    1. Create the application registration

        Creating the application registration allows the use of Azure Active Directory to authenticate users and to request access to user resources. The registered app provides the bot access to the Bot Framework Service for sending and receiving authenticated messages. 

        ```cmd
        az ad app create --display-name "TeamsAuthenticationRegistration" --password "<<your password>>" --available-to-other-tenants
        ```

        |Parameter|Description|Notes|
        |:---|:---|:---|
        |display-name|The name to display in the resources list|<img src="" width="300"/>|
        |password|App password, aka 'client secret'. The password must be at least 16 characters long, contain at least 1 upper or lower case alphabetical character, and contain at least 1 special character.|Copy and save to a file. To be used later.|

    Set Azure Active Directory Graph entities needed for role based access. This step also produces the **app id** to use in the next step.

         

    Save the **app id** and **password** to a file.

    1. Start deployment via ARM template which cerates the bott channel registration. This step also produces the subscription id to use in the next step.

        ```cmd
        az deployment create --name "TeamsAuthentication" --template-file "..BotBuilder-Samples\samples\python\57.teams-auth\deploymentTemplates\template-with-new-rg.json" --location "westus" --parameters appId="<<get it from previous step>>" appSecret="<<your password>>" botId="TeamsAuthentication" botSku=F0 newAppServicePlanName="<<your plan name>>" newWebAppName="TeamsAuthentication" groupName="<<your group name>>" groupLocation="westus" newAppServicePlanLocation="westus"
        ```

    1. Optionally, check App Id and Password settings

        ```cmd
        az webapp config appsettings list -g mm-python-group -n TeamsAuthenticationNew --subscription  <<your subscription id>>
        ```

    You can run the az cli commands from within Visual Studio Code using the [AZ CLI extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azurecli).  See also [The Azure Command-Line Interface (CLI)](https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest).

## Test the bot using the Bot Emulator

Before deploying the bot to Azure let's test it on the local machine.

1. In a terminal window, navigate to `*\BotBuilder-Samples\samples\python\46.teams-auth`.
1. Launch the application.

    ```cmd
    python app.py
    ```

    The following message is displayed:

    ![teams Authentication app emulator](../Media/Python/teams-app-emulator.PNG)

1. Open a new terminal window and execute this command:

    ```cmd
    ngrok http -host-header=rewrite 3978
    ```

    You get an output similar to this:

    ![teams Authentication app ngrok](../Media/Python/teams-app-ngrok.PNG) 

1. Copy the **https forwarding** address which is similar to this: `https://e075240a.ngrok.io`. 
1. Add to it `api/messages`, so the address is similar to this `https://e075240a.ngrok.io/api/messages`. Save the address to a file. 
This the **end point** to connect with the bot running locally.
1. Activate the Bot Framework Emulator. 
1. Click the **Open Bot** button.
1. In the **Bot URL** box, enter the end point address you saved before such as `https://e075240a.ngrok.io/api/messages`.
1. In the **Microsoft App ID** box enter the *app id* you saved earlier.  
1. In the **Microsoft App  password** box enter same *password* you saved earlier.
    > NOTE
    > If you restart ngrok, the end point URL changes and you must restart the emulator and enter the new URL.
1. Click the **Connect** button.
1. Wait for the emulator to connect to the bot. You should see a *201 Created* message in the ngrok terminal window,
1. Enter any text in the emulator box, for example *hello*.
1. The welcome card is displayed. This means that the bot is working correctly.

    ![teams Authentication app emulator welcome card](../Media/Python/teams-conversation-app-emulator-welcome-card.PNG) 

## Create the identity provider

You need an identity provider that can be used for authentication. In this procedure you'll use an Azure Active Directory provider. Follow the steps described in [Create the identity provider](https://docs.microsoft.com/microsoftteams/platform/bots/how-to/authentication/add-authentication#create-the-identity-provider).

At this time you will also configure the identity provider connection and register it with the bot channel registration created earlier. 
Copy and save the connection name you used to a file.  

## Deploy the bot to Azure final steps

 1. Before performing the deployment step, you must prepare the bot code as described below.

    1. Create `manifest.zip` file
        1. Navigate to `*\BotBuilder-Samples\samples\python\46.teams-auth\teams_app_manifest` directory.
        1. In your editor, open the `manifest.json` file.  To the `id` and `bot Id` variables assign the **app id** obtained before.
        1. Save the file.
        1. Select all the files in the directory and zipped them up in a file such as `manifest.zip`.

    1. Create `app.zip` file
        1. Navigate to `*\BotBuilder-Samples\samples\python\46.teams-auth` directory.
        1. In your editor, open the `config.py` file.  
        Assign the following values:
            1. `APP_ID = os.environ.get("MicrosoftAppId", "")` assign the *app id* you saved earlier.
            1. `APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")` assign the password you saved earlier. 
            1. `CONNECTION_NAME = os.environ.get("ConnectionName", "")` assign the identity provider connection name you created earlier.
        1. Save the file.
        1. Select all the files in the directory and zipped them up in a file such as `app.zip`.

    1. Deploy the bot

        ```cmd
        az webapp deployment source config-zip --resource-group "mm-python-group" --name "TeamsAuthentication" --src "..BotBuilder-Samples\samples\python\57.teams-Authentication-bot\app.zip"
        ```
        if you navigate to the Azure portal, you should see the bot app registration and app service listed as shown below. 
        ![teams Authentication bot deployed](../Media/Python/teams-conversation-bot-deployed.PNG).

At this point the bot is ready to be used from within Teams.

## Using the bot within Teams

1. Activate your Microsoft Teams.
1. In the lower left, left panel, click the **Apps** icon.
1. In the right panel, click the **Upload a custom app** link.
1. Navigate to the directory `..BotBuilder-Samples\samples\python\57.teams-Authentication-bot\teams_app_manifest`.
1. Select the `manifest.zip` file.
1. Click the **Open** button.
1. In the Teams wizard window, click the arrow in the **Add** button and select *Add to a team* or *Add to a chat*.

    ![teams Authentication bot wizard](../Media/Python/teams-conversation-bot-wizard.PNG) 

1. In the next window, select the team or chat where to add the bot.
1. Click the **Setup a bot** button.
1. After the bot is set, you can start entering the allowed requests 
1. If you enter *Show Welcome*, the welcome card is displayed. This means that the bot is working correctly and can be used within Teams.

     ![teams Authentication bot welcome card](../Media/Python/teams-conversation-bot-welcome-card.PNG) 

You can interact with the bot by sending it a message, or selecting a command from the command list. The bot will respond to the following strings.

|Personal|Group|Team|Result|
|:---|:---|:---|:---|
|Show Welcome<br/>Mention Me<br/>Message All Members|Show Welcome<br/>Mention Me<br/>Message All Members|Show Welcome<br/>Mention Me<br/>Message All Members|Welcome card for you to interact with<br/>Mention the user<br/>1-on-1 message to each member in the current Authentication|

## Appendix

### Test the bot running on your local machine using Teams

1. Activate your Microsoft Teams.
1. In the lower left, left panel, click the **Apps** icon.
1. In the right panel, click the **Upload a custom app** link.
1. Navigate to the directory `*\BotBuilder-Samples\samples\python\47.teams-auth\teams_app_manifest`.
1. Select the `manifest.zip` file.
1. Click the **Open** button.
1. In the Teams wizard window, click the arrow in the **Add** button and select *Add to a team* or *Add to a chat*.

    ![teams conversation bot wizard](../Media/Python/teams-conversation-bot-wizard.PNG) 

1. In Teams, open **App Studio**.
1. Click the **Manifest editor** tab.
1. In the left panel, click the **Create a new app** button.
1. In the **Details** section, click the **App details**.
1. Enter the following  info:
    1. **Short name**. Enter *conversationBot*.  
    1. Click the **Generate** button under **App ID**. You an ID similar to this *772998ff-7fed-4275-b4e3-485cbf312850*. `Why do we need this?`
    1. **Package Name**. Enter *com.teams.devapp*.
    1. **Version** Enter *1.0.0*.
    1. **Short Description**. Enter *Testing conversation bot*.
    1. **Long Description**. Enter *Testing conversation bot*.
    1. **Developer name**. Your name.
    1. **Website**. The name of your website. For example, *https://www.microsoft.com*.
    1. **Privacy statement** web address. For example, *https://www.teams.com/privacy*.
    1. **Terms of use** web address. For example, *https://www.teams.com/termsofuse*.
1. In the left panel, in the **Capabilities** section, click the **Bots** link.
1. Click the **Set up** button. 
1. In the **New bot** tab, enter the following information:
    1. **Name**. Enter *conversationBot*.
    1. **Scope**. Check all 3 boxes.
    1. Click the **Create** button.
1. Copy the **Bot ID** (string under conversationBot) and save it to a file to use it later.
1. Click the **Generate new password** button, copy the password and save it to a file to use it later.
1. In a terminal window execute the following command: `ngrok http -host-header=rewrite 3978`.
Make sure that the port number is set properly in the `config.py` file such as `PORT = 3978`. This is the number to use in the ngrok command.
1. Copy the **https** forwarding address to a file. Notice this forwarding address changes every time you restart ngrok.  
1. Keep **ngrok** running.  
1. In the **Messaging endpoint** section in the **Bot endpoint address** enter the ngrok address you saved earlier followed by */api/messages*. This is an example: `https://d1dbb0d8.ngrok.io/api/messages`. 
1. Press **Enter** (on your keyboard) to save the address.
