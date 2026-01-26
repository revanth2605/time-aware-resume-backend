import { useState } from "react";
import { BASE_URL } from "../api/api";
import Navbar from "../components/Navbar";

function UploadCode() {

  const [skill, setSkill] = useState("Python");
  const [visibility, setVisibility] = useState("private");   // NEW
  const [message, setMessage] = useState("");

  async function handleUpload() {

    const token = localStorage.getItem("token");

    const response = await fetch(`${BASE_URL}/upload/code`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({
        skill_name: skill,
        visibility: visibility     // NEW
      })
    });

    const data = await response.json();
    setMessage(JSON.stringify(data));
  }

  return (
    <>
      <Navbar />

      <div>

        <h2>Upload Code</h2>

        <input
          value={skill}
          onChange={(e) => setSkill(e.target.value)}
        />

        <br /><br />

        <b>Visibility:</b>

        <br />

        <label>
          <input
            type="radio"
            value="public"
            checked={visibility === "public"}
            onChange={() => setVisibility("public")}
          />
          Public
        </label>

        <label style={{ marginLeft: "10px" }}>
          <input
            type="radio"
            value="private"
            checked={visibility === "private"}
            onChange={() => setVisibility("private")}
          />
          Private
        </label>

        <br /><br />

        <button onClick={handleUpload}>
          Upload Code
        </button>

        <p>{message}</p>

      </div>
    </>
  );
}

export default UploadCode;
