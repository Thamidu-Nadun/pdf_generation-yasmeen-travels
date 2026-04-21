import fs from 'fs';

const content = fs.readFileSync('mail3.txt', 'utf-8');

const data = {
    'to_email': 'nadunrz101@gmail.com',
    'subject': 'Email from Email SMTP',
    'body': content,
    'mail_type': 'confirmation'
}

const send = async () => {
    try {
        console.log('Sending POST request to http://localhost:5000/email');
        console.log('Data keys:', Object.keys(data));
        console.log('Body length:', data.body.length);

        const res = await fetch('http://localhost:5000/email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        console.log("Response status:", res.status);
        const result = await res.json();
        console.log("Response body:", result);
    } catch (e) {
        console.error("Error:", e.message);
        console.error("Error code:", e.code);
        if (e.cause) {
            console.error("Cause:", e.cause);
        }
    }
}

send();