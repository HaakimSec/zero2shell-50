const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.send(`
        <h1>Zero2Shell Lab 15: SSRF to RCE Chain</h1>
        <p>Use the URL preview feature via: <code>/api/preview?url=http://example.com</code></p>
    `);
});

// VULNERABLE ENDPOINT: Blindly trusts user input for server-side requests
app.get('/api/preview', async (req, res) => {
    const targetUrl = req.query.url;

    if (!targetUrl) {
        return res.status(400).json({ error: "Missing 'url' parameter" });
    }

    try {
        // The server acts as a proxy, fetching whatever destination the user specifies
        const response = await axios.get(targetUrl, { timeout: 3000 });
        res.set('Content-Type', response.headers['content-type']);
        return res.send(response.data);
    } catch (error) {
        return res.status(500).json({ 
            error: "Failed to fetch preview resource", 
            details: error.message 
        });
    }
});

app.listen(PORT, () => {
    console.log(`Public web shell facing tier active on port ${PORT}`);
});
