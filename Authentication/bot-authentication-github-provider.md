# Bot authentication via GitHub provider


## Create a GitHub application

1. In your browser, log in your GitHub account.
1. Navigate to [GitHub Apps](https://github.com/settings/apps);
1. Click the **OAuth Apps** link in the left panel.
1. Click the **New OAuth App** button.
1. Confirm your password.
1. Enter the following information:
    1. **Application name** - The name of the application.
    1. **HomePage URL** - https://dev.botframework.com.
    1. **Application description** - The intent of this application.
    1. **Authorization callback URL** - https://token.botframework.com/.auth/web/redirect.
1. Click the **Register application** button.
1. Upload a logo.
1. Click the **Update application** button.
1. Notice the *Client Id* and *Client Secret*. We'll need them when setting the bot OAuth connection string.
