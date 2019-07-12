# Add Dialogs to .NET Hello World Bot

## Table of Content

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Create the Project](#create-the-project)
- [Run Out of the Box](#run-out-of-the-box)
- [Modify the Bot](#modify-the-bot)
- [Deploy the Bot](#deploy-the-bot)
- [Connect Skype Channel](#connect-skype-channel)


## Overview

![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png)![star](../../Media/Generic/star.png)

This article describes how to add dialogs to the HelloWorld Bot created in the article [Hello World Bot](HelloWorldBot.md).  

### About Dialogs

- A dialog encapsulates application logic like a function in a program.
- It allows you to perform a specific task, such as gathering the details of a user’s profile, and then possibly of reusing the code when needed.
- Dialogs can also be chained together in **DialogSets**.

- The **Microsoft Bot Builder SDK v4** includes two built-in features to help you manage conversations using dialogs:

  - **DialogSets**
    - They are a collection of dialogs. To use dialogs, you must first create a dialog set and add dialogs to it.
    - A dialog can contain only a single or multiple **waterfall steps**.

  - **Prompts**
    - They provide the methods you can use to ask users for different types of information. For example, a text input, a multiple choice, or a date or number input. 
    - A prompt dialog uses at least two functions, one to prompt the user to input data, and another function to process and respond to the data.


## Prerequisites

Before you proceed, assure that the following requirements are satisfied:

1. [Visual Studio 2019 (or higher)](https://visualstudio.microsoft.com/vs/) with the following workloads:
    1. ASP.NET and web development
    1. Azure development
    1. .NET Core cross-platform development
1. [Bot Builder V4 SDK Template for Visual Studio](https://marketplace.visualstudio.com/items?itemName=BotBuilder.botbuilderv4)
1. [Bot Framework Emulator](https://github.com/Microsoft/BotFramework-Emulator/releases/)
1. [A Microsoft Azure Subscription](https://azure.microsoft.com/en-us/free/?v=18.23)

## Add Dialogs to HelloWorld Bot

The Bot described in the [Hello World Bot](HelloWorldBot.md) example has inherent limitations such as:

- All code logic is in the main path.
- No easy way to encapsulate individual logic.
- No way to reuse code logic 
- As the code gets bigger it will be not manageable.

### Dialogs to the Rescue

Dialogs allow us to solve the previous issues. To add dialog the **HelloWorld** Bot follow these steps:

1. In Visual Studio 2017 or higher, open the project created following the steps described in [Hello World Bot](HelloWorldBot.md) article. 
1. In the *Solutiuon Explorer*, right-click on the project name and select **Manage NuGet Packages**.

    ![Manage NuGet Packages](../../Media/Examples/Dialogs\NuGetPackages.PNG)
1. In the package manager left pane, click the **Browse** link in the upper left.
1. In the search box, enter *microsoft bot dialogs*.
1. Select the **Microsoft.Bot.Builder.Dialogs** package.
1. In the right pane, click the **Install** button.

