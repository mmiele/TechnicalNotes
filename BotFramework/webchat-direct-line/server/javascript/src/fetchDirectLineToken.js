const fetch = require('node-fetch');

// Calls Direct Line API to generate a Direct Line token
// Provides user ID in the request body to bind the user ID to the token
module.exports = async function fetchDirectLineTokenAsync(secret, userId) {
    const response = await fetch('https://directline.botframework.com/v3/directline/tokens/generate', {
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${secret}`,
        },
        method: 'post',
        body: JSON.stringify({ user: { id: userId } })
    });

    if (!response.ok) {
        throw new Error(`Direct Line token API call failed with status ${response.status}`);
    }

    const responseJson = await response.json();

    const { conversationId, token, expires_in: expiresIn } = responseJson;

    return { conversationId, token, expiresIn };
};