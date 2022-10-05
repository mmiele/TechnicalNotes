---
Installing and using GitHub desktop app
last update: 10/04/22
---

# GitHub dektop app

## Install GitHub desktop on Ubuntu using `dpkg` command

1. Go to [GitHub Desktop Release](https://github.com/shiftkey/desktop/releases) page to download `deb` format file, provided via direct link.

1. Open your terminal `Ctrl + Alt + T`, head over to your directory where your installer has been saved and run the commands shown below with sudo privileges.

    ``` cmd
    sudo dpkg -i <fileName>.deb
    ```

    > [!NOTE] Replace fileName with actual file name with deb extension. 

1. Fix dependency errors and broken packages for GitHub Desktop

    ``` cmd
    sudo apt update && sudo apt install -f
    ```

The command `sudo apt update` updates package lists. The command `sudo apt install -f` fixes dependencies and broken packages if any.
Then reinstall with dpkg command again


1. Run application

Once the installation is done, you can now run Github desktop from the application launcher.

For more information, see [Install GitHub Desktop on Ubuntu or Ubuntu-based distributions](https://meshworld.in/install-github-desktop-on-ubuntu-20-04-or-ubuntu-based-distributions/). 

