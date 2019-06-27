# How Bots Work

A bot is an app that users interact with in a conversational way via **text**, **graphics** (such as cards or images), or **speech**.
Every interaction between the user and the bot generates an **activity**. 

The Bot Framework Service, which is a component of the Azure Bot Service, sends information between the user's bot-connected app (such as Facebook, Skype, Slack, etc. which we call the channel) and the bot. Each channel may include additional information in the activities they send. 

Before creating bots, it is important to understand how a bot uses activity objects to communicate with its users. Let's first take a look at activities that are exchanged when we run a simple echo bot.

![echo_bot_sequence_diagram](../media/echo_bot_sequence_diagram.PNG)

The 2 activity types illustrated in the picture are: **conversation update** and **message**. 
The Bot Framework Service may send a conversation update when a party joins the conversation. For example, on starting a conversation with the Bot Framework Emulator, you will see two conversation update activities (one for the user joining the conversation and one for the bot joining). To distinguish these conversation update activities, check whether the members added property includes a member other than the bot. The message activity carries conversation information between the parties. 
In an echo bot example, the message activities are carrying simple text and the channel will render this text. Alternatively, the message activity might carry text to be spoken, suggested actions or cards to be displayed. 
In this example, the bot created and sent a message activity in response to the inbound message activity it had received. However, a bot can respond in other ways to a received message activity; it is not uncommon for a bot to respond to a conversation update activity by sending some welcome text in a message activity. More information can be found in welcoming the user.
