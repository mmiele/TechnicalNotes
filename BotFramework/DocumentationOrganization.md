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
    1. **Debug**
        1. [Debug a bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-debug-bot?view=azure-bot-service-4.0). How to debug your bot using an integrated development environment (IDE) such as Visual Studio or Visual Studio Code and the Bot Framework Emulator.
        1. [Debug with the emulator](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-debug-emulator?view=azure-bot-service-4.0&tabs=csharp). The Bot Framework Emulator is a desktop application that allows bot developers to test and debug their bots, either locally or remotely.
        1. [Debug a bot with inspection middleware](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-debug-inspection-middleware?view=azure-bot-service-4.0&tabs=csharp). Debug your bot using inspection middleware. This feature allows the Bot Framework Emulator to debug traffic into and out of the bot in addition to looking at the current state of the bot.
        1. [Debug your bot using transcript files](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-debug-transcript?view=azure-bot-service-4.0). Creation and use of a bot transcript file to provide a detailed set of user interactions and bot responses for testing and debugging.
    1. Deploy
        1. [Deploy your bot to Azure](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-deploy-az-cli?view=azure-bot-service-4.0&tabs=csharp). How to prepare your bot for deployment, deploy your bot to Azure, and test your bot in Web Chat.
        1. [Set up continuous deployment](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-build-continuous-deployment?view=azure-bot-service-4.0). How to enable continuous deployment to automatically deploy code changes from your source repository to Azure. 
    1. **Manage**
        1. [Manage a bot](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-manage-overview?view=azure-bot-service-4.0). How to manage a bot using the Azure portal.
        1. [Bot analytics](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-manage-analytics?view=azure-bot-service-4.0).  Provides conversation-level reporting on user, message, and channel data.
        1. **Channels**
            1. [Connect a bot to channels](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-manage-channels?view=azure-bot-service-4.0). A channel is a connection between the bot and communication apps. You configure a bot to connect to the channels you want it to be available on.
            1. [Implement channel-specific functionality](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-channeldata?view=azure-bot-service-4.0). Implement channel-specific functionality, you can pass native metadata to a channel in the activity object's *channel data* property.
            1. [Connect a bot to Cortana](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-cortana?view=azure-bot-service-4.0). Cortana is a speech-enabled channel that can send and receive voice messages in addition to textual conversation. A bot intended to connect to Cortana should be designed for speech as well as text.
            1. **Direct Line**
                1. [About Direct Line](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-directline?view=azure-bot-service-4.0). The Direct Line channel is an easy way to integrate your bot into your mobile app, webpage, or other application.
                1. [Connect to Direct Line](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-directline?view=azure-bot-service-4.0). Enable your own client application to communicate with your bot by using the Direct Line channel.
                1. [Connect to Direct Line Speech](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-directlinespeech?view=azure-bot-service-4.0). Configure your bot to allow client applications to communicate with it through the Direct Line Speech channel.
                1. **Direct Line App Service Extension**
                    1. [Direct Line App Service Extension](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-directline-extension?view=azure-bot-service-4.0). The direct line app service extension allows clients to connect directly with the host, where the bot is located.
                    1. [Configure .NET bot for extension](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-directline-extension-net-bot?view=azure-bot-service-4.0). How to update a bot to work with named pipes, and how to enable the direct line app service extension in the Azure App Service resource where the bot is hosted.
                    1. [Create .NET Client to Connect to Direct Line App Service Extension](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-directline-extension-net-client?view=azure-bot-service-4.0). How to create a .NET client in C# which connects to the direct line app service extension.
                    1. [Use WebChat with the direct line app service extension](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-directline-extension-webchat-client?view=azure-bot-service-4.0). How to use WebChat with the direct line app service extension.
                    1. [Use direct line app service extension within a VNET](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-directline-extension-vnet?view=azure-bot-service-4.0). How to use the Direct Line App Service Extension with an Azure Virtual Network (VNET).
                1. [Email](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-email?view=azure-bot-service-4.0). Connect a bot to an email account.
                1. [Facebook](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-facebook?view=azure-bot-service-4.0). Connect a bot Facebook.
                1. [GroupMe](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-groupme?view=azure-bot-service-4.0). Connect a bot to use GroupMe.
                1. [Kik](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-kik?view=azure-bot-service-4.0).Connect a bot to Kik.
                1. [LINE](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-line?view=azure-bot-service-4.0). Connect a bot to LINE.
                1. [Microsoft Teams](https://docs.microsoft.com/en-us/azure/bot-service/channel-connect-teams?view=azure-bot-service-4.0). Connect a bot to Microsoft Teams.
                1. [Skype](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-skype?view=azure-bot-service-4.0). Connect a bot to Skype. 
                1. [Skype for Business](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-skypeforbusiness?view=azure-bot-service-4.0). Connect a bot to Skype for Business.
                1. [Slack](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-slack?view=azure-bot-service-4.0). Connect a bot to Slack.
                1. [Telegram](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0). Connect a bot to Telegram.
                1. [Twilio](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-twilio?view=azure-bot-service-4.0). Connect a bot to Twilio. 
                1. [Additional Channels](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-additional-channels?view=azure-bot-service-4.0). A few additional channels are available as an adapter. 
        1. [Configure bot settings](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-manage-settings?view=azure-bot-service-4.0). Settings, such as Display name, Icon, and Application Insights, can be viewed and modified on a bot **Settings** blade.
        1. [Configure speech priming](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-manage-speech-priming?view=azure-bot-service-4.0). Speech priming improves the recognition of spoken words and phrases that are commonly used in your bot. 

    1. **Migrate**
        1. [Migration overview](https://docs.microsoft.com/en-us/azure/bot-service/migration/migration-overview?view=azure-bot-service-4.0&tabs=csharp). Migration from v3 to v4 overview. 
        1. [Differences between the v3 and v4 .NET SDK](https://docs.microsoft.com/en-us/azure/bot-service/migration/migration-about?view=azure-bot-service-4.0)
        1. [Differences between the v3 and v4 JavaScript SDK](https://docs.microsoft.com/en-us/azure/bot-service/migration/migration-about-javascript?view=azure-bot-service-4.0)
        1. [.NET migration quick reference](https://docs.microsoft.com/en-us/azure/bot-service/migration/net-migration-quickreference?view=azure-bot-service-4.0)
        1. [JavaScript migration quick reference](https://docs.microsoft.com/en-us/azure/bot-service/migration/javascript-migration-quickreference?view=azure-bot-service-4.0)
        1. [Migrate a .NET v3 bot to a .NET Framework v4 bot](https://docs.microsoft.com/en-us/azure/bot-service/migration/conversion-framework?view=azure-bot-service-4.0)
        1. [Migrate a .NET v3 bot to a .NET Core v4 bot](https://docs.microsoft.com/en-us/azure/bot-service/migration/conversion-core?view=azure-bot-service-4.0)
        1. [Using .NET v3 user state in a v4 bot](https://docs.microsoft.com/en-us/azure/bot-service/migration/csharp-user-state-using?view=azure-bot-service-4.0)
        1. [Migrate a Javascript v3 bot to a v4 bot](https://docs.microsoft.com/en-us/azure/bot-service/migration/conversion-javascript?view=azure-bot-service-4.0)
1. **Reference**
    1. .NET SDK v4
    1. JavaScript SDK v4
    1. REST
        1. NET SDK v3
        1. Node.js SDK v3
        1. Entities and activity types
1. **Resources**
    1. Virtual Assistant
        1. [Overview](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-virtual-assistant-introduction?view=azure-bot-service-4.0). Virtual Assistant solution provides a set of core foundational capabilities and full control over the end user experience.
        1. [Template Introduction](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-virtual-assistant-template?view=azure-bot-service-4.0). The Virtual Assistant Template brings together a number of best practices we've identified through the building of conversational experiences and automates integration of components that we've found to be highly beneficial to Bot Framework developers. 
    1. Skills
        1. [Overview](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-skills-overview?view=azure-bot-service-4.0). Developers can compose conversational experiences by stitching together re-usable conversational capabilities, known as Skills.
    1. WebChat
        1. [Overview](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-webchat-overview?view=azure-bot-service-4.0).
        The Bot Framework Web Chat component is a highly customizable web-based client for the Bot Framework V4 SDK. The Bot Framework SDK v4 enables developers to model conversation and build sophisticated bot applications.
        1. [Customization](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-webchat-customization?view=azure-bot-service-4.0).  How to customize the Web Chat samples to fit your bot.
    1. [FAQ](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-resources-bot-framework-faq?view=azure-bot-service-4.0). Answers to some frequently asked questions about the Bot Framework.
    1. [Get Support](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-resources-links-help?view=azure-bot-service-4.0). Resources for additional information and support for developing bots with the Bot Framework.
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





 
