# Bot Framework Notes

## Overview

A bot is a **web service** that implements a **conversational interface** and communicates with the **Bot Framework Service** to send and receive messages and events.

![robot icon](../Media/miscellanea/robot.PNG)

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

- [Bot Framework SDK](https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-overview?view=azure-bot-service-3.0) for developing bots
- [Bot Framework Tools](https://github.com/Microsoft/botbuilder-tools) to cover end-to-end bot development workflow
- [Bot Framework Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0) to send and receive messages and events between bots and channels
- [Azure Bot Service Documentation](https://docs.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0)
- [Bot Framework SDK](https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-overview?view=azure-bot-service-3.0)
- [Team Blog](https://dev.botframework.com/)
- Github repositories:
  - https://github.com/MicrosoftDocs/bot-docs-pr/
  - https://github.com/Microsoft/BotBuilder-Samples/
  - https://github.com/Microsoft/botbuilder-tools/
- [Azure portal](https://ms.portal.azure.com/#home)
- [Conversational chatbot for hotel reservations on Azure](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/ai/commerce-chatbot)
- [Introduction to Microsoft Azure Bot Service & LUIS](https://medium.com/@ashish_fagna/introduction-to-microsoft-azure-bot-service-luis-language-understanding-8826d29d013e)
- [What is Language Understanding (LUIS)?](https://docs.microsoft.com/en-us/azure/cognitive-services/luis/what-is-luis)
- [Microsoft Conversational AI tools enable developers to build, connect and manage intelligent bots](https://azure.microsoft.com/en-us/blog/microsoft-conversational-ai-tools-enable-developers-to-build-connect-and-manage-intelligent-bots/)
- [Bot Framework Stack Overflow](https://stackoverflow.com/questions/tagged/botframework)
- [Logging and Debugging with Azure Bot Service](https://azure.github.io/learnAnalytics-AdvancedFeaturesforMicrosoftBotFramework/lab01-logging_chat_conversations/0_README.html)
- [Popular Chatbot Frameworks](https://discover.bot/bot-talk/beginners-guide-bots/popular-chatbot-frameworks/?ref=GADW-cpc-y2fxvw5g&pk_campaign=GADW-Search)
- [Creating a Hello World! Bot (MS Bot Framework V4)](http://aihelpwebsite.com/Blog/EntryId/1030/Creating-a-Hello-World-Bot-MS-Bot-Framework-V4-Preview-Edition) ![star](../Media/miscellanea/star.PNG)![star](../Media/miscellanea/star.PNG)![star](../Media/miscellanea/star.PNG)![star](../Media/miscellanea/star.PNG)
- [ASP.NET MVC Tutorial](https://www.tutorialspoint.com/asp.net_mvc/index.htm)
- [Implement custom storage for your bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-custom-storage?view=azure-bot-service-4.0)
- [Talking to my Bot](https://github.com/Microsoft/ailab/tree/master/BuildAnIntelligentBot) ![star](../Media/miscellanea/star.PNG)![star](../Media/miscellanea/star.PNG)![star](../Media/miscellanea/star.PNG)
