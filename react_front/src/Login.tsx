import axios from "axios";
import { useState } from "react";

function Login() {
    const [loginData, setLoginData] = useState([]);

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

    return (
        <>
            <h1>Login</h1>
            <form onSubmit={onLoginSubmit}>
                <input type="text" name="id" placeholder="id" />
                <input type="text" name="password" placeholder="password" />
                <button type="submit">Login</button>
            </form>
            {loginData.map((item: any) => (
                <div key={item.message}>
                    <p>{item.message}</p>
                    <p>{item.password}</p>
                    <p>{item.token}</p>
                </div>
            ))}
        </>
    )
}

export default Login;