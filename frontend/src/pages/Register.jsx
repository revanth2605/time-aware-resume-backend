import { useState } from "react";
import { BASE_URL } from "../api/api";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";

function Register() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");   // ✅ NEW
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  async function handleRegister() {

    try {
      const response = await fetch(`${BASE_URL}/register`, {
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
        navigate("/");   // go to login
      } 
      else {
        setMessage(data.message || "Registration failed");
      }

    }
    catch (err) {
      console.log(err);
      setMessage("Server error");
    }
  }

  return (
    <>
      <Navbar />

      <div>

        <h2>Register</h2>

        <input
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <br /><br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <br /><br />

        <button onClick={handleRegister}>
          Register
        </button>

        <p>{message}</p>

      </div>
    </>
  );
}

export default Register;
