import { useState } from "react";
import { BASE_URL } from "../api/api";

function Login() {

  const [username, setUsername] = useState("");
  const [message, setMessage] = useState("");

  async function handleLogin() {
    console.log("Login button clicked");

    try {
      const response = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          username: username
        })
      });

      const data = await response.json();
      console.log("Response:", data);

      if (data.success) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "/dashboard";
      } else {
        setMessage(data.message);
      }
    }
    catch (error) {
      console.log("Error:", error);
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
        placeholder="Enter username"
      />

      <br /><br />

      <button onClick={handleLogin}>
        Login
      </button>

      <p>{message}</p>

    </div>
  );
}

export default Login;
