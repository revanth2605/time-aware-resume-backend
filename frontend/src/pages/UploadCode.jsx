import { useState } from "react";
import { BASE_URL } from "../api/api";
import Navbar from "../components/Navbar";

function UploadCode() {

  const [skill, setSkill] = useState("Python");
  const [visibility, setVisibility] = useState("private");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleUpload() {

    try {

      setLoading(true);
      setMessage("");

      const token = localStorage.getItem("token");

      const response = await fetch(`${BASE_URL}/upload/code`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
          skill_name: skill,
          visibility: visibility
        })
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage("Upload failed");
        return;
      }

      setMessage(
        `✅ Code uploaded for ${data.skill.skill_name}
Score: ${Math.round(data.skill.current_score)}
Visibility: ${data.skill.visibility}`
      );

    } catch{
      setMessage("Server error");
    } finally {
      setLoading(false);
    }
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

        <button onClick={handleUpload} disabled={loading}>
          {loading ? "Uploading..." : "Upload Code"}
        </button>

        <p>{message}</p>

      </div>
    </>
  );
}

export default UploadCode;
