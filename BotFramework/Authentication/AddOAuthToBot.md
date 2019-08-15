# Add OAuth to a bot

This topic shows how to use **Azure Bot Service** authentication to develop a bot which can be authenticated by various identity providers such as Azure Active Directory (Azure AD), GitHub and so on.

## Overview

You will create a sample bot that connects to [Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview) using **Azure AD authentication**. You will use code from a GitHub repository, and learn how to 

- [Create an Azure Bot Service resource](#Create-an-azure-bot-service-resource)
- [Create an Azure AD application](#Create-an-azure-ad-application)
- [Prepare the bot sample code](#prepare-the-bot-sample-code)
- [Use the emulator to test the bot](#use-the-emulator-to-test-the-bot)

The completed bot performs a few simple tasks against an Azure AD application, such as checking and sending an email, or displaying who you are and who your manager is. To do this, the bot will use a token from an Azure AD application against the `Microsoft.Graph` library.


## Create an Azure Bot Service resource

You need an **Azure Bot Service** resource to register the bot with Azure and make it available to the users, for example over the web through channels. To create this resource, please follow the steps described in this article: [Register a bot with Bot Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-quickstart-registration?view=azure-bot-service-3.0).


## Create an Azure AD application


## Prepare the bot sample code



## Use the emulator to test the bot