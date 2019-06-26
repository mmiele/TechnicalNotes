<link href="css/custom.css" rel="stylesheet"></link> 

# Bot Framework Architecture

## Overview

In the last few years, evolution of devices, platforms and applications have improved user experience and, as a result, expectations. Voice activated digital assistants like Siri and Cortana allow users to interact with services and information in new different ways. 

Perhaps it is time to replace the old web forms with more natural, conversational interaction with users.

In 2016 conference Microsoft introduced its [Bot Framework](https://dev.botframework.com/), which provides a platform for developers to build **intelligent conversation agents**, aka **bots**, and connect them via growing list of **channels** such as Skype, Facebook Messenger,Slack, Telegram and an embed web chat widget.
If combined with the services and APIs offered in [Microsoft Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/), such as [Language Understanding Intelligent Service (LUIS)](https://azure.microsoft.com/en-us/services/cognitive-services/language-understanding-intelligent-service/), bots have the potential to provide rich and useful interactions with users.

## Bot Framework Architecture

The following picture provides a bird's eye view of the Microsoft Bot Framework architecture.
![Bot Architecture](media/bot_architecture_2.png)

Let's describe the various components.

### Your Bot

Typically, a bot is implemented as a **standard Web service which exposes a REST API**. You can implement it with any web technology stack you prefer. 
Microsoft provides a [Bot Framework SDK](https://docs.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0) for .NET (C#} and JavaScript (Node.js).
Both SDKs are free, open source and hosted on GitHub at this location: [botframework-sdk](https://github.com/microsoft/botframework-sdk)
The Bot Framework SDK gives you two primary tools for building your interface: **Dialogs** and **FormFlows**.

1. **Dialogs** give you the most flexibility, but also require you to manage message parsing, conversation orchestration and managing any state your dialog may need to reference.
1. **FormFlows** provide a guided conversation with the ability to provide options, do input validation, and confirm user responses. They are a good choice for replacing existing web forms with something more like a natural conversation.

You can call Dialogs from within other Dialogs, allowing you to structure your bot conversations with composition and reuse. You can also launch a FormFlow from within a Dialog, allowing you to mix and match both freer form LUIS-driven dialogs and guided information collection.


### Language Understanding Intelligent Service (LUIS)

The Bot Framework SDK facilitates the integration of [LUIS](https://azure.microsoft.com/en-us/services/cognitive-services/language-understanding-intelligent-service/), models for language understanding. LUIS helps a bot to parse messages to understand the user’s intent and any related entities.

#### Training LUIS

LUIS actively learns based on the messages it receives, so it is continuously improving. You can review recognized and unrecognized messages to further train LUIS for your model.
The [LuisDialog](https://docs.botframework.com/en-us/csharp/builder/sdkreference/d8/df9/class_microsoft_1_1_bot_1_1_builder_1_1_dialogs_1_1_luis_dialog.html) class in the Bot Framework SDK makes it simple to wire up a LUIS application to call the appropriate methods on your Dialog based on Intent parsing, and passing any parsed entities along the way.

### Beyond Text

The latest release of the Bot Framework SDK includes support for richer content such as **cards**, **carousels** and **buttons**. Channels that are not capable to display the richer content, and others (like SMS texting) fall back to text.

You can also integrate other services with your bot, such as the [Bing Speech API](https://www.microsoft.com/cognitive-services/en-us/speech-api/) and Bing search APIs like [Web](https://www.microsoft.com/cognitive-services/en-us/bing-web-search-api), [Image](https://www.microsoft.com/cognitive-services/en-us/bing-image-search-api) and [Video](https://www.microsoft.com/cognitive-services/en-us/bing-video-search-api). 
You can also integrate big data analytics and machine learning through technologies such as [Cortana](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-cortana?view=azure-bot-service-4.0), to help build even more intelligent bots.

## References

| Topic | Description |
| :--- | :--- |
| [Bot Framework SDK](https://www.appliedis.com/the-bot-framework/) <img src="" width="200"/> | Architectural notes |
| [LUIS]((https://azure.microsoft.com/en-us/services/cognitive-services/language-understanding-intelligent-service/))|Language Understanding Intelligent Service|
