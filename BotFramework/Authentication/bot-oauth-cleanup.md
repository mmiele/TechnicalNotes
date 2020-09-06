# Bot Framework Architecture

## Overview





## Architectural notes

The following architecture highlights the **Bot Connector** position between the **Bot** and the **Channels**.

![Bot Framework architecture](../../Media/Authentication/bot-framework-architecture-simple.PNG)

The Bot Framework Service lives in the cloud and takes on the role of translating the data from the APIs of multiple supported Channels into the Bot Framework protocol in a form that a bot can understand.
This allows the bot to communicate with multiple channels, without having to understand which Channel the data is coming from. A client application makes REST calls to the Bot Framework Service, specifically to the **Bot Framework Adapter** which sends the outbound request back towards the Bot Framework Service, which eventually talks to the channel.

The Bot Framework Service works both inbound and outbound whereas the **Bot Connector Service** works only outbound. The Bot Connector Service exchanges information between bot and channel (user) by passing an Activity object.
When a bot sends a request to the Bot Connector Service, it must include information that the Connector service can use to **verify its identity**. Likewise, when the Connector service sends a request to your bot, it must include information that the bot can use to verify its identity.

## Bot connector service, adapters, and authentication


- [Connectors](https://docs.microsoft.com/en-us/connectors/connectors)
- [Create a bot with the Bot Connector service](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-quickstart?view=azure-bot-service-4.0)
- [Authentication](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-authentication?view=azure-bot-service-4.0) as it applies to bot/connector connection
- [BotFrameworkAdapter class](https://docs.microsoft.com/en-us/javascript/api/botbuilder/botframeworkadapter?view=botbuilder-ts-latest)

![Bot Framework architecture](../../Media/Authentication/azure-bot-service-architecture.PNG)




## References

- [Enterprise-grade conversational bot](https://docs.microsoft.com/azure/architecture/reference-architectures/ai/conversational-bot) - Architecture
- [The Bot Framework](https://www.ais.com/the-bot-framework/) - Architecture
- [Bot Framework Service vs Bot Connector Service](https://stackoverflow.com/questions/59984775/bot-framework-service-vs-bot-connector-service)
