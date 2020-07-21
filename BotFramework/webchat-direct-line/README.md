# Direct Line Token Sample

This sample demonstrates how to implement WebChat in a way that does not expose your Direct Line secret to the browser.

## Motivation

### Hiding the WebChat secret

When embedding WebChat into a site, you must provide either your Direct Line secret or a Direct Line token so that WebChat can communicate with the bot. The Direct Line secret can be used to access all of the bot's conversations, and it doesn't expire. A Direct Line token can only be used to access a single conversation, and it does expire. See the [Direct Line Authentication documentation](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-authentication?view=azure-bot-service-4.0) for more information.

Therefore, embedding WebChat using the Direct Line secret directly is strongly discouraged because it would expose your secret on the client-side. Instead, the recommended approach is to exchange the secret for a Direct Line token on the server-side. This sample shows how to obtain and use the token.

### Avoiding user impersonation

WebChat allows you to specify a user ID on the client-side, which will be sent in activities to the bot. However, this is susceptible to user impersonation because a malicious user could modify their user ID. Since the user ID typically isn't verified, this is a security risk if the bot stores sensitive data keyed on the user ID. For example, the built-in [user authentication support in Azure Bot Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-authentication?view=azure-bot-service-4.0) associates access tokens with user IDs.

To avoid impersonation, the recommended approach is for the server to bind a user ID to the Direct Line token. Then any conversation using that token will send the bound user ID to the bot. However, if the client is going to provide the user ID to the server, it is important for the server to validate the ID somehow (see below). Otherwise, a malicious user could still modify the user ID being sent by the client.

To keep things simple, this sample generates a random user ID on the server-side and binds it to the Direct Line token. While this mitigates impersonation concerns, the downside is that users will have a different ID every time they talk to the bot. If you need a consistent and validated user ID, see the [Direct Line user token sample](https://github.com/navzam/user-direct-line-token-sample).

## Architecture

This sample contains three components:
- **The backend API** performs the Direct Line token acquisition. It generates a random user ID that will be bound to the Direct Line token.
- **The UI** is static HTML/JS that could be hosted using any web server. It makes a POST request to the backend API and uses the resulting Direct Line token to render WebChat.
- **The bot** is a bare-bones bot that responds to every activity by sending the user's ID.  

Depending on the scenario, the backend API could be called from a client (such as a single-page application) or a server (such as a more traditional web app). After receiving the Direct Line token, the caller can then use it to render Web Chat, and the bot will receive the randomly-generated user ID on every activity.

## Code highlights

### Constructing the user ID

In this sample, the user is anonymous, so the API randomly generates a user ID:

<details><summary>JavaScript</summary>

```js
// server.js

async function generateRandomUserId() {
    const buffer = await randomBytesAsync(16);
    return `dl_${buffer.toString('hex')}`;
}
```

</details>

<details><summary>C#</summary>

```csharp
// DirectLineTokenController.cs

private static string GenerateRandomUserId()
{
    byte[] tokenData = new byte[16];
    using var rng = new RNGCryptoServiceProvider();
    rng.GetBytes(tokenData);

    return $"dl_{BitConverter.ToString(tokenData).Replace("-", "").ToLower()}";
}
```

</details>

The user ID is prefixed with "dl_" as required by the [Direct Line token API](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-authentication?view=azure-bot-service-4.0#generate-token).

### Retrieving a user-specific Direct Line token

The API calls the Direct Line API to retrieve a Direct Line token. Notice that we pass the user ID in the body of the request:

<details><summary>JavaScript</summary>

```js
// fetchDirectLineToken.js

const response = await fetch('https://directline.botframework.com/v3/directline/tokens/generate', {
    headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${secret}`,
    },
    method: 'post',
    body: JSON.stringify({ user: { id: userId } })
});
```

</details>

<details><summary>C#</summary>

```csharp
// DirectLineTokenService.cs

httpClient.BaseAddress = new Uri("https://directline.botframework.com/");

...

var fetchTokenRequestBody = new { user = new { id = userId } };

var fetchTokenRequest = new HttpRequestMessage(HttpMethod.Post, "v3/directline/tokens/generate")
{
    Headers =
    {
        { "Authorization", $"Bearer {directLineSecret}" },
    },
    Content = new StringContent(JsonSerializer.Serialize(fetchTokenRequestBody), Encoding.UTF8, MediaTypeNames.Application.Json),
};

var fetchTokenResponse = await _httpClient.SendAsync(fetchTokenRequest, cancellationToken);
```

</details>

The resulting Direct Line token will be bound to the passed user ID.

### Calling the API and rendering WebChat

The UI calls the API and uses the resulting Direct Line token to render WebChat:

```js
// index.html

const res = await fetch('http://localhost:3000/api/direct-line-token', { method: 'POST' });
const { token } = await res.json();

window.WebChat.renderWebChat(
    {
    directLine: window.WebChat.createDirectLine({ token }),
    },
    document.getElementById('webchat')
);
```

Note that we do *not* specify a user ID when initiating WebChat. Direct Line will handle sending the user ID to the bot based on the token.

## Running the sample locally

### Prerequisites
- A registered Bot Framework bot (see [documentation on registering a bot with Azure Bot Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-quickstart-registration?view=azure-bot-service-3.0))

### Run the bot
1. Navigate to the `bot` directory.
1. Fill in the environment variables in the `.env` file, according to the following table:
    | Variable | Description | Example value |
    | -------- | ----------- | ------------- |
    | `PORT` | The port on which the bot server will run. | 3978 |
    | `MICROSOFT_APP_ID` | The app ID of the registered Bot Framework bot. Can be found in the Azure Bot Channels Registration resource. | |
    | `MICROSOFT_APP_SECRET` | The app secret of the registered Bot Framework Bot. Issued during registration. | |
1. Run `npm install` to install the required dependencies.
1. Run `npm start` to start the bot.
1. Run `ngrok` to expose your bot to a public URL. For example:
    ```bash
    ngrok http -host-header=rewrite 3978
    ```
1. Update the messaging endpoint in your Bot Channels Registration to the ngrok URL. For example: `https://abcdef.ngrok.io/api/messages`

### Run the API

The sample API is available in multiple languages. Choose one and expand the corresponding section for specific steps.

<details><summary>JavaScript API</summary>

1. Navigate to the `api/javascript` directory.
1. Fill in the environment variables in the `.env` file. See the table below for descriptions.
1. Run `npm install` to install the required dependencies.
1. Run `npm start` to start the server.

| Variable | Description | Example value |
| -------- | ----------- | ------------- |
| `PORT` | The port on which the API server will run. | 3000 |
| `DIRECT_LINE_SECRET` | The Direct Line secret issued by Bot Framework. Can be found in the Azure Bot Channels Registration resource after enabling the Direct Line channel. |  |

</details>

<details><summary>C# API</summary>

1. Add the required secrets to the .NET Core secret manager. See the table below for descriptions.
    ```bash
    cd ./api/csharp
    dotnet user-secrets set "DirectLine:DirectLineSecret" "YOUR-DIRECT-LINE-SECRET-HERE"
    ```
1. (optional) Change the port specified in `./Properties/launchSettings.json`.
1. Run `dotnet run` to start the server. (Alternatively, open and run the project in Visual Studio.)

| Variable | Description | Example value |
| -------- | ----------- | ------------- |
| `DirectLine:DirectLineSecret` | The Direct Line secret issued by Bot Framework. Can be found in the Azure Bot Channels Registration resource after enabling the Direct Line channel. |  |

</details>

### Run the UI
1. Navigate to the `ui` directory.
1. Open `index.html` in a browser. (Alternatively, you can serve `index.html` on `localhost` using a web server, or use a local development server such as the [Live Server Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer).)