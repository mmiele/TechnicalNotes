# Azure Bot Service Documentation Organization  

The following is the [Azure Bot Service Documentation](https://docs.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0) organization. It comprises the following major areas: 

1. **[Azure Bot Service Documentation](https://docs.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0)**. This is the home page that contains introductory information and links to major areas.
1. **Overview**. Describes the basics of a bot and the main steps to build one. It also contains a **[what's new](https://docs.microsoft.com/en-us/azure/bot-service/what-is-new?view=azure-bot-service-4.0)** section.
1. **Quickstart**. It contains examples to enable the customer to jump start with the bot technology. For example, [Create a bot with Azure Bot Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-quickstart?view=azure-bot-service-4.0).
1. **Tutorials**. This area contains complete walkthroughs showing how to use some aspects of the bot technology. For example, [Tutorial: Use QnA Maker in your bot to answer questions](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-add-qna?view=azure-bot-service-4.0&tabs=csharp).
1. **Samples**. it links to the [BotBuilder-Samples](https://github.com/Microsoft/BotBuilder-Samples/blob/master/README.md) in GitHub. Samples are designed to illustrate scenarios a customer needs to build great bots! See also [README](https://github.com/Microsoft/BotBuilder-Samples/blob/master/README.md).
1. **Concepts**. This section contains conceptual topics that lay the foundation to help the customer understand bot technology.
    1. [How bots work](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0&tabs=csharp). It describes the details of bot workings.  
    1. [Managing state](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-state?view=azure-bot-service-4.0
). It describes how a bot state is handled and why is needed.
    1. [Dialogs library](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0
). Dialogs are a central concept and provide a useful way to manage a conversation.
    1. [Middleware](). Middleware is simply a class that sits between the adapter and the bot logic, added to the adapter's middleware collection during initialization.
    1. [User authentication](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-authentication?view=azure-bot-service-4.0). Explains  authentication so a bot can use external services on behalf of the user.   
    1. [Manage bot resources](https://docs.microsoft.com/en-us/azure/bot-service/bot-file-basics?view=azure-bot-service-4.0&tabs=csharp). Explains managing resources used by a bot.
1. **How To**. It contains guidelines and examples to perform essential tasks. From bot design to development, from debugging to deployment, from management to migration.
    1. **Design** 
        1. [Principles of bot design](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-principles?view=azure-bot-service-4.0). Contains best bot design practices. 
        1. [First interaction](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-first-interaction?view=azure-bot-service-4.0). The first interaction between the user and bot is critical to the user experience. Here you find information that can help to provide effective first steps.  
        1. [Design and control conversation flow](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-conversation-flow?view=azure-bot-service-4.0). Designing and handling conversation flow.
        1. [Design the user experience](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-user-experience?view=azure-bot-service-4.0). The elements of a good user experience design.  
        1. **Patterns** Bot design patterns.
            1. [Knowledge base](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-pattern-knowledge-base?view=azure-bot-service-4.0). Principles of a knowledge base bot.  
            1. [Handoff to humans](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-pattern-handoff-human?view=azure-bot-service-4.0). Transitioning conversations from bot to humans.
            1. [Bots in apps](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-pattern-embed-app?view=azure-bot-service-4.0). How to embed a bot in an app.
            1. [Bots in websites](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-pattern-embed-web-site?view=azure-bot-service-4.0). How to embed a bot in a website.

    1. **Develop**
        1. [Send and receive text message](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-send-messages?view=azure-bot-service-4.0&tabs=csharp).  Describes techniques to send and receive messages. 
        1. [Add media to messages](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-add-media-attachments?view=azure-bot-service-4.0&tabs=csharp). Adding media attachments, such as images, video, audio, and files to messages.
        1. [Use button for input](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-add-suggested-actions?view=azure-bot-service-4.0&tabs=csharp). Enabling a bot to present buttons that the user can tap to provide input.
        1. [Save user and conversation data](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-v4-state?view=azure-bot-service-4.0&tabs=csharp). Using state management and storage objects to manage and persist state.
        1. [Prompt user for input](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-primitive-prompts?view=azure-bot-service-4.0&tabs=csharp). Prompt (ask) the user for information (input).
        1. [Send welcome message to users](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-send-welcome-message?view=azure-bot-service-4.0&tabs=csharp). Starting a meaningful conversation with the user.
        1. [Send proactive notifications to users](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-proactive-message?view=azure-bot-service-4.0&tabs=csharp). Sending out of flow messages to the user.
        1. [Implement sequential conversation flow](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-dialog-manage-conversation-flow?view=azure-bot-service-4.0&tabs=csharp). How to implement simple conversation flow by creating prompts and calling them from a waterfall dialog.
        1. [Add natural language understanding to your bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-v4-luis?view=azure-bot-service-4.0&tabs=csharp). Adding LUIS to a flight booking application to recognize different intents and entities contained within user input.
        1. [Use QnA Maker to answer questions](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-qna?view=azure-bot-service-4.0&tabs=cs). Provide a conversational question and answer layer over your data.
        1. [Use multiple LUIS and QnA models](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-dispatch?view=azure-bot-service-4.0&tabs=cs). Determine which LUIS model or QnA Maker knowledge base best matches the user input.
        1. [Create advanced conversation flow using branches and loops](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-dialog-manage-complex-conversation-flow?view=azure-bot-service-4.0&tabs=csharp). Manage simple and complex conversation flows using the dialogs library.
        1. [Reuse dialogs](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-compositcontrol?view=azure-bot-service-4.0&tabs=csharp). Create independent dialogs to handle specific scenarios, breaking a large dialog set into more manageable pieces.
        1. [Handle user interruptions](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-handle-user-interrupt?view=azure-bot-service-4.0&tabs=csharp). Some common ways to handle user interruptions.
        1. [Write directly to storage](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-howto-v4-storage?view=azure-bot-service-4.0&tabs=csharp). How to read and write data to storage using **Memory Storage**, **Cosmos DB**, **Blob Storage**, and **Azure Blob Transcript Store**.
        1. [Add authentication to your bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-authentication?view=azure-bot-service-4.0&tabs=csharp%2Cbot-oauth). Adding OAuth to a bot to access external resources (services) on behalf of the user.
        1. [Implement custom storage for your bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-custom-storage?view=azure-bot-service-4.0). Semantics of the bot’s interactions with the **Azure Bot Service** and the **Store**.
        1. [Add telemetry to your bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-telemetry?view=azure-bot-service-4.0). Enable a bot to send event data to telemetry services.
        1. [Use Direct Line Speech in your bot](https://docs.microsoft.com/en-us/azure/bot-service/directline-speech-bot?view=azure-bot-service-4.0).  Exchange messages between the **Direct Line Speech** channel and your bot.
    1. **Test** 
        1. [Unit test bots](https://docs.microsoft.com/en-us/azure/bot-service/unit-test-bots?view=azure-bot-service-4.0&tabs=csharp). Create unit tests for bots. Use assert to check for activities returned by a dialog turn against expected values. Use assert to check the results returned by a dialog. Create different types of data driven tests. Create mock objects for the different dependencies of a dialog (i.e. LUIS recognizers, etc.).
    1. **Debug**.
    1. Deploy
    1. Manage
    1. Migrate
1. **Reference**
    1. .NET SDK v4
    1. JavaScript SDK v4
    1. REST
        1. NET SDK v3
        1. Node.js SDK v3
        1. Entities and activity types
1. **Resources**
    1. Virtual Assistant
    1. Skills
    1. WebChat
    1. FAQ
    1. Get Support
    1. Channel reference
    1. Guide to identifiers
    1. App Insights keys
    1. User agent requests
    1. Bot review guidelines
    1. Bot Framework Activity schema
    1. Bot Framework Card schema
    1. Bot Framework Transcript schema
    1. Bot Service Compliance
1. **Troubleshoot**





 
