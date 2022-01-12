---
title: Ubuntu 
description: Collect notes about Ubuntu
author: michael
last update: 01/09/2022
---

# Ubuntu notes



## Install Visual Studio Code

Open your terminal (`Ctrl + Alt + T`). Then perform the steps below.

Foolow the steps as described in the section 
2- Install Visual Studio Code On Ubuntu 20.04 (LTS) and 20.10 Using Terminal, in the article [How to Install Visual Studio Code On Ubuntu 20.04](https://linuxhint.com/install_use_vs_code_ubuntu/). 



## Install GitHub desktop 

Open your terminal (`Ctrl + Alt + T`). Then perform the steps below.

The following command upload version 2.6.3, but you can select the version you want. 

``` cmd
sudo wget https://github.com/shiftkey/desktop/releases/download/release-2.6.3-linux1/GitHubDesktop-linux-2.6.3-linux1.deb`
```
```cmd
sudo apt-get install gdebi-core
```
```cmd
sudo gdebi GitHubDesktop-linux-2.6.3-linux1.deb
```

To acctivate the app, go to the **Applications** window and search for `github`. 
Select the app.  

For mmore information, see [Install GitHub Desktop on Ubuntu 20.04 or Ubuntu-based distributions](https://meshworld.in/install-github-desktop-on-ubuntu-20-04-or-ubuntu-based-distributions/).

> [!NOTE]
> I had login problems when trying to access my GitHub repo. To solve the issue, I created a personal access token (PAT) and use it instead of the password to login. For more information, see [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).



## How to Install VirtualBox on Ubuntu 20.04 LTS

### What is VirtualBox?
VirtualBox is a free, open-source and cross-platform software that lets you create, run, and manage **virtual machines** (VMs) on your computer.  

- With Oracle VM VirtualBox you can create one or more VMs on a single physical server. 
- Virtual machines are computers that use the hardware components of the host computer, each running its own operating system. 
- VirtualBox supports the installation of MS Windows, Linux, BDS, and MS-DOS on the installed VMs.

Below we'll explain how to install a VirtualBox on Ubuntu 20.04 LTS  system using the CLI commands.


Open a terminal window and execute the commands shown below.

In order to install the latest VirtualBox, you need to have the **Multiverse** repository enabled on your system. By default this repository is disabled. Enter the following command as root in order to enable the repository and also update your system’s repository index with that on the internet. 

```cmd
sudo add-apt-repository multiverse && sudo apt-get update
```
When running the previous command, if you get the error `add-apt-repository` command not found, execute the following command first:

```cmd
sudo apt install software-properties-common
```
Now, enter the following command to install VirtualBox:

```cmd
sudo apt install virtualbox
```
You can launch VirtualBox directly through the terminal by entering the following command:

```cmd
virtualbox
```
Exit the Terminal by entering this command:

```cmd
exit
```







For more information, see [How to Install VirtualBox on Ubuntu 20.04 LTS](https://vitux.com/how-to-install-virtualbox-on-ubuntu/).





## Miscellanea

- [How to Uninstall An Application In Ubuntu](https://techwiser.com/uninstall-applications-ubuntu/)