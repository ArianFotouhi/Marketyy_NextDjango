"use client"
import './styles/styles.css';
import React, { useState, useEffect } from 'react';
// import { redirect } from 'next/navigation';
import { useRouter } from 'next/navigation'

export default function LoginPage() {
    const router = useRouter()

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    // Function to handle login
    const handleLogin = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://127.0.0.1:8000/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                throw new Error('Login failed');
            }

            // Assuming the response is a JSON object containing the token
            const data = await response.json();
            const token = data.token;

            // Store the token in localStorage for future use
            localStorage.setItem('token', token);

            // Redirect to the /devices route
            // redirect('/devices');
            router.push('/devices')

        } catch (error) {
            console.error('Login error:', error.message);
            setError('Failed to log in');
        }
    };

    // Effect to check if the user is already logged in
    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) {
            // Redirect to the /devices route if the user is already logged in
            router.push('/devices')
        }
    }, []);

    return (
        <div className="login-container">
            <h2>Login Page</h2>
            <div className='form-holder'>
            <form onSubmit={handleLogin}>
                <div className="form-group">
                    <label>Username</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                {error && <div className="error-message">{error}</div>}
                <button type="submit">Login</button>
            </form>
            </div>

        </div>
    );
}
