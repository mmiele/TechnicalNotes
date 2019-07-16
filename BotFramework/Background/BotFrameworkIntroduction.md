# Bot Framework Notes

## Overview

A bot is a **web service** that implements a **conversational interface** and communicates with the **Bot Framework Service** to send and receive messages and events.

![robot icon](../../Media/Generic/robot.PNG)

The Bot Framework Service is one of the components of the Azure Bot Service and [Bot Framework](https://dev.botframework.com/) .
Bots allow a user to interact with a computer as she would interact with a human, or at least with an intelligent robot. They are used to perform simple, repetitive tasks, such as taking a dinner reservation or gathering profile information, or to automate systems that may no longer require direct human intervention. 

Azure Bot Service provides an integrated environment which allows to build, connect, test, deploy, and manage intelligent bots.
For more information, see [Azure Bot Service Documentation]((https://docs.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0)) and [Bot Framework SDK](https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-overview?view=azure-bot-service-3.0).

Users converse with a bot via **text**, **interactive cards**, and **speech**. A bot interaction can be a quick question and answer, or it can be a sophisticated conversation that intelligently provides access to services.

Bots are a lot like modern web applications, living on the internet and use APIs to send and receive messages. What's in a bot varies widely depending on what kind of bot it is. Modern bot software relies on a stack of technology and tools to deliver increasingly complex experiences on a wide variety of platforms. However, a simple bot could just receive a message and echo it back to the user with very little code involved.

Bots can do the same things other types of software can do - read and write files, use databases and APIs, and do the regular computational tasks. 

> [!WARNING]
> What makes bots unique is their use of mechanisms generally reserved for human-to-human communication.

Azure Bot Service and Bot Framework offer:

- Core component and hosting environment for creating bots
- Bot builder SDK for developing
- Bot connector service to connect the bots to channels

After the bot is created, you can add intelligence to the bot with Microsoft Cognitive Services such as Language Understanding Service (LUIS), Vision, Speech and many other capabilities so the bot can see, hear, understand and interact in more natural ways.

## References

The following is a road map that can help navigating through many documentation layers both internal and external to Microsoft. It tries to give you a compass to go through the labyrinth.   

|Topic|Description
|:---|---|
|<img width=500/>|**Microsoft**|
|[Azure Bot Service Documentation](https://docs.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0) | Microsoft Bot Framework Documentation. Azure Bot Service and Bot Framework provide tools to build, test, deploy, and manage intelligent bots all in one place.
|[Microsoft Bot Framework SDK](https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-overview?view=azure-bot-service-3.0)|Microsoft open source SDKs, tools, and services which enable developers to build, test, and connect bots.
|[Bot Builder Samples](https://github.com/Microsoft/BotBuilder-Samples/)|Microsoft Bot Samples on GitHub.
|[Bot Framework Tools](https://github.com/Microsoft/botbuilder-tools/)|Microsoft collection of cross-platform command line tools.
[Bot Builder V4 SDK Templates](https://marketplace.visualstudio.com/items?itemName=BotBuilder.botbuilderv4)|Visual Studio >NET templates .NET will let you quickly set up a conversational AI bot using core AI capabilities.|
[Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator/releases/)|Desktop client app to test bots.|
|[Azure portal](https://ms.portal.azure.com/#home)|Azure portal to deploy a bot. 
|[Team Blog](https://dev.botframework.com/)|Bot Framework team blog.
|[Hotel reservations chantbot on Azure](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/ai/commerce-chatbot)|Applicable to businesses that need to integrate a conversational chatbot into applications.|
|[What is Language Understanding (LUIS)?](https://docs.microsoft.com/en-us/azure/cognitive-services/luis/what-is-luis)|Cloud-based API service that applies custom machine-learning intelligence to a user's conversational, natural language text to predict overall meaning, and pull out relevant, detailed information.|
|[Microsoft Conversational AI tools enable developers to build, connect and manage intelligent bots](https://azure.microsoft.com/en-us/blog/microsoft-conversational-ai-tools-enable-developers-to-build-connect-and-manage-intelligent-bots/)|Conversational AI is the next user interface (UI) wave in computing. |
|[Logging and Debugging with Azure Bot Service](https://azure.github.io/learnAnalytics-AdvancedFeaturesforMicrosoftBotFramework/lab01-logging_chat_conversations/0_README.html)|Microsoft labs for learning to log and debugg with Azure Bot Service|
|[Bot Framework additional resources](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-resources-links-help?view=azure-bot-service-4.0)|These resources provide additional information and support for developing bots with the Bot Framework|
|<img width=500/>|**Others**|
|[Hello World! Bot](http://aihelpwebsite.com/Blog/EntryId/1030/Creating-a-Hello-World-Bot-MS-Bot-Framework-V4-Preview-Edition) | Create a Hello World! Bot with Bot Framework V4 ![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png) |
|[Talking to my Bot](https://github.com/Microsoft/ailab/tree/master/BuildAnIntelligentBot) |![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png)
|[Microsoft Azure Bot Service & LUIS](https://medium.com/@ashish_fagna/introduction-to-microsoft-azure-bot-service-luis-language-understanding-8826d29d013e)|Introduction to Microsoft Azure Bot Service & LUIS|
|[Bot Framework Stack Overflow](https://stackoverflow.com/questions/tagged/botframework)|Questions tagged **botframework** on StackOverflow |
|[Popular Chatbot Frameworks](https://discover.bot/bot-talk/beginners-guide-bots/popular-chatbot-frameworks/?ref=GADW-cpc-y2fxvw5g&pk_campaign=GADW-Search)|Covers some of the most common bot building frameworks out there: Amazon Lex, Dialogflow, and Microsoft Bot Framework.|
|[ASP.NET MVC Tutorial](https://www.tutorialspoint.com/asp.net_mvc/index.htm)|This tutorial provides a complete picture of the MVC framework and teaches you how to build an application using this tool.|
