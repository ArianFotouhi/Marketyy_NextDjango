"use client";

import Link from 'next/link'
import {redirect} from 'next/navigation';

async function getDevices() {

    const endpoint = 'http://127.0.0.1:8000/api/devices/';
    const res = await fetch(endpoint, { cache: 'no-store' });

    if (!res.ok) {
        // Redirect to the login page if response code is not 200
        redirect('/login');        
        // throw new Error(`Failed to fetch data with code ${res.status}`);
    }

    return res.json();
}

export default async function Devices() {
    const devices = await getDevices()

    return (
        <div className="flex flex-col items-center mt-2">
            <h1 className="text-4xl">My Devices</h1>
            
            <div className="mt-5 flex flex-col gap-2">
                { devices.map(device => 
                    <p className="text-xl text-blue-500 hover:text-blue-800" key={device.id}>
                        <Link href={`/devices/${device.slug}`}>
                            { device.name }
                        </Link>
                    </p>
                ) }
            </div>

            <Link href="/devices/create/">
                <button className="btn btn-primary mt-4">Add Device</button>
            </Link>
        </div>        
    )
}