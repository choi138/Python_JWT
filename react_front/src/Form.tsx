import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function Form() {
    const [data, setData] = useState<any>();

    const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        try {
            let res = await axios.post('http://127.0.0.1:8000/register', e.target);
            let data = res.data;
            setData(data);
            console.log(data);
        } catch (err) {
            console.log(err);
        }
    }

    const [loginData, setLoginData] = useState<any>();

    const onLoginSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        try {
            let res = await axios.post('http://127.0.0.1:8000/login', e.target);
            let data = res.data;
            setLoginData(data);
            console.log(data);
        } catch (err) {
            console.log(err);
        }
    }

    const [message, setMessage] = useState<any>();

    const onProfileSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        try {
            let res = await axios.post('http://127.0.0.1:8000/profile', e.target);
            let data = res.data;
            setMessage(data);
            console.log(data);
        } catch (err) {
            console.log(err);
        }
    }

    return (
        <>
            <div>
                <h1>Register</h1>
                <form onSubmit={onSubmit}>
                    <input type="text" name="name" placeholder="name" />
                    <input type="text" name="id" placeholder="id" />
                    <input type="text" name="password" placeholder="password" />
                    <input type="text" name="email" placeholder="email" />
                    <input type="text" name="phone" placeholder="phone" />
                    <button type="submit">Register</button>
                </form>
                {data ?
                    <div>
                        <p>{data.message}</p>
                        <p>{data.token}</p>
                    </div>
                    : null}
                <Link to='/'>Go to Home</Link>
                <br />
                <Link to='/login'>Go to Login</Link>
            </div>
            <br />

            <div>
                <h1>Login</h1>
                <form onSubmit={onLoginSubmit}>
                    <input type="text" name="email" placeholder="email" />
                    <input type="text" name="id" placeholder="id" />
                    <input type="text" name="password" placeholder="password" />
                    <button type="submit">Login</button>
                </form>
                {loginData ?
                    <div>
                        <p>{loginData.message}</p>
                        <p>{loginData.password}</p>
                        <p>{loginData.token}</p>
                    </div>
                    : null}
            </div>
            <br />

            <div>
                <h1>Profile</h1>
                <form onSubmit={onProfileSubmit}>
                    <input type="text" placeholder="token" name="token" />
                    <button type="submit">Profile</button>
                </form>
                <div >
                    {message ?
                        <>
                            <p>{message.message}</p>
                            <p>name: {message.name}</p>
                            <p>id: {message.id}</p>
                            <p>email: {message.email}</p>
                            <p>phone: {message.phone}</p>
                        </>
                        : null}
                </div>
            </div>
        </>
    )
}

export default Form