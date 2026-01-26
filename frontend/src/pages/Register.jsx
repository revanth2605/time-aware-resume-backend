import { useState } from "react";
import { BASE_URL } from "../api/api";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";

function Register() {

  const [username, setUsername] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  async function handleRegister() {

    const response = await fetch(`${BASE_URL}/register`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: username
      })
    });

    const data = await response.json();

    if (data.success) {
      navigate("/");
    } else {
      setMessage(data.message);
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

        <button onClick={handleRegister}>
          Register
        </button>

        <p>{message}</p>

      </div>
    </>
  );
}

export default Register;
