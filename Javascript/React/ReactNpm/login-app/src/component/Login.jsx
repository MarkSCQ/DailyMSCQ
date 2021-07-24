import React, { useState } from 'react'
import "./Login.css"
export default function Login() {
    // variable name, hook name
    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")


    return (
        <div className="login">
            <form className="lgoin__form">
                <h1>
                    Login ⚔️🏹🛡️🗡️🔪💣🔫
                </h1>
                <input type="name" placeholder="User Name" value={name} onChange={(e) => setName(e.target.value)} />

                <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />

                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />

                <button type="submit" className="submit__btn">sb</button>
            </form>
        </div>
    )
}
