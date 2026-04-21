import fetch from 'node-fetch';

const test = async () => {
    try {
        // Test 1: Simple GET request
        console.log("Test 1: Testing GET /email");
        const res1 = await fetch('http://localhost:5000/email');
        const data1 = await res1.json();
        console.log("Response status:", res1.status);
        console.log("Response data:", data1);
    } catch (e) {
        console.log("Error:", e.message);
    }
}

test();
