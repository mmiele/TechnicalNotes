const express = require('express');
const crypto = require('crypto');
const { promisify } = require('util');

const fetchDirectLineTokenAsync = require('./fetchDirectLineToken');

const randomBytesAsync = promisify(crypto.randomBytes);

// Verify required environment variables
const port = enforceEnvironmentVariable('PORT');
const directLineSecret = enforceEnvironmentVariable('DIRECT_LINE_SECRET');

// Create Express application
const app = express();
app.use(express.json());

// Endpoint for generating a Direct Line token bound to a random user ID
app.post('/api/direct-line-token', async (req, res) => {
    // Set CORS header. For simplicity, allow requests from all origins
    // You should restrict this to specific domains
    res.header('Access-Control-Allow-Origin', '*');

    // Generate a random user ID to use for DirectLine token
    const randomUserId = await generateRandomUserId();

    // Get user-specific DirectLine token and return it
    let directLineTokenResponse;
    try {
        directLineTokenResponse = await fetchDirectLineTokenAsync(directLineSecret, randomUserId);
    } catch (e) {
        if (e instanceof Error) {
            res.status(400).send({ message: e.message });
            return;
        }

        throw e;
    }

    const response = { ...directLineTokenResponse, userId: randomUserId };
    res.send(response);
});

app.listen(port, () => {
    console.log(`API running on port ${port}`);
});

// Generates a random user ID
// Prefixed with "dl_", as required by the Direct Line API
async function generateRandomUserId() {
    const buffer = await randomBytesAsync(16);
    return `dl_${buffer.toString('hex')}`;
}

// Tries to return the value of an environment variable
// Quits if the variable doesn't exist
function enforceEnvironmentVariable(name) {
    const value = process.env[name];
    if (value === undefined || value.length === 0) {
        console.error(`Required environment variable not set: ${name}`);
        process.exit();
    }

    return value;
}