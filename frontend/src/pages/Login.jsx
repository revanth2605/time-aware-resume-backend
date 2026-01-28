import { useState } from "react";
import { BASE_URL } from "../api/api";

function Login() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");   // ✅ NEW
  const [message, setMessage] = useState("");

  async function handleLogin() {

    try {
      const response = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          username: username,
          password: password
        })
      });

      const data = await response.json();

      if (data.success) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "/dashboard";
      } 
      else {
        setMessage(data.message || "Login failed");
      }

    }
    catch (error) {
      console.log(error);
      setMessage("Server error");
    }
  }

  return (
    <div>

      <h2>Login</h2>

      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />

      <br /><br />

      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />

      <br /><br />

      <button onClick={handleLogin}>
        Login
      </button>

      <br /><br />

      {/* ✅ REGISTER LINK */}
      <p>
        New user?{" "}
        <span
          style={{ color: "blue", cursor: "pointer" }}
          onClick={() => window.location.href = "/register"}
        >
          Register here
        </span>
      </p>

      <p>{message}</p>

    </div>
  );
}

export default Login;
