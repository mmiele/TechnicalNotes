# Teams Echobot 

This article shows how to install a simple echo bot in Teams using App Studio. 
You can use the example code on GitHub at this location: [Teams echo bot](https://github.com/microsoft/botbuilder-dotnet/tree/josh/echo/tests/Teams/52.Teams-echo-bot).


## Teams Setup

1. In Teams, open **App Studio**. 
1. Click the **Manifest editor** tab.
1. In the left panel, click the **Create a new app** button.
1. In the **Details** section, click the **App details**. 
1. Enter the following  info:
    1. **Short name**. Enter *TeamsEchoBot*.  
    1. Click the **Generate** button under **App ID**. You an ID similar to this *772998ff-7fed-4275-b4e3-485cbf312850*. 
    1. **Package Name**. Enter *com.teams.devapp*.
    1. **Version** Enter *1.0.0*.
    1. **Short Description**. Enter *Testing simple teams echo bot*.
    1. **Long Description**. Enter *Testing simple teams echo bot*.
    1. **Developer name**. Your name.
    1. **Website**. The name of your website. For example, *https://www.microsoft.com*
    1. **Privacy statement** web address. For example, *https://www.teams.com/privacy*
    1. **Terms of use** web address. For example, *https://www.teams.com/termsofuse*
1. In the left panel, in the **Capabilities** section, click the **Bots** link.
1. Click the **Set up** button. 
1. In the **New bot** tab, enter the following informatin:
    1. **Name**. Enter *TeamsEchoBot*.
    1. **Scope**. Check all 3 boxes.
    1. Click the **Create** button.
1. Copy the **Bot ID** (string under TeamsEchoBot) and save it to a file. You will need it later
1. Click the **Generate new password** button, copy the password and save it to a file. You will need it later. 
1. In a terminal window execute the following command: `ngrok http -host-header=rewrite 3978`.
1. Copy the https forwarding address to a file.
1. Keep **ngrok** running.  
1. In the **Messaging endpoint** section in the **Bot endpoint address** enter the ngrok address you saved earlier followed by */api/messages*. For example: *https://d1dbb0d8.ngrok.io/api/messages*. 
1. Press **Enter** (on your keyboard) to save the address. 


## Bot Setup

1. Clone the repository at [botbuilder-dotnet](https://github.com/microsoft/botbuilder-dotnet/tree/josh/echo/tests/Teams).
1. In Visual Studio, navigate to the `52.teams-echo-bot` folder and open the `appsettings.json` file.
1. Assign the bot **App ID** and **Password** you saved earlier. For example:

```json
{
  "MicrosoftAppId": "772998ff-7fed-4275-b4e3-485cbf312850",
  "MicrosoftAppPassword": "M@XlmJPuYNjFmE:[h2AvMBOzNBuP9=43"
}
```

1. **Save** the `appsettings.json` file.

1. Open the file *Properties/launchSettings.json*. Assure that this setting exists: ` "applicationUrl": "http://localhost:3978/"`.

1. Open the file *TeamsAppManifest/manifest.json*. Assign to the `id` and `botId` variables the **Bot ID* value you saved earlier.  
1. **Save** the `manifest.json` file.
1. Zip the 3 files contained in the folder. 
1. Navigate to the `52.teams-echo-bot` folder.
1. Run the project (F5). 
1. A browser window will open at this local address `localhost:3978/`. 


## Finish Teams Setup

1. In Teams click **Test and distribute** in the left panel in the **Finish** section.
1. Click the **Install** button.

    <table>
    <thead>
    <tr>
    <th align="left">To install bot in a personal chat...</th>
    <th align="left">To install in a group chat...</th>
    <th align="left">To install in team chat...</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td align="left">1. Click <code>Add</code> button</td>
    <td align="left">1. Click the down arrow to the right of the <code>Add</code> button <br> 2. Click <code>Add to Chat</code> <br> 3. Search for and select your group chat <br> 4. Click the <code>Set up bot</code> button <br> <strong>Note:</strong> There must be at least 1 message in a group chat for it to be searchable</td>
    <td align="left">1. Click the down arrow to the right of the <code>Add</code> button <br> 2. Click <code>Add to Team</code> <br> 3. Search for and select your team <br> 4. Click the <code>Set up a bot</code> button</td>
    </tr>
    </tbody>
    </table>
    <p><strong>Note:</strong> If you send an unsupported string in a group chat or personal chat the bot will respond with an error message. This is because it's missing data that comes with messages that orignates from a team or group chat.</p>
    <table>
    <thead>
    <tr>
    <th align="left">Supported strings in personal chat</th>
    <th align="left">Supported strings in group chat</th>
    <th align="left">supported strings in team chat</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td align="left">N/A</td>
    <td align="left"><code>show members</code></td>
    <td align="left"><code>show members</code> <br> <code>show channels</code> <br> <code>show details</code></td>
    </tr>
    </tbody>
    </table>
