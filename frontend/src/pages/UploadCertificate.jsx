import { useState } from "react";
import { BASE_URL } from "../api/api";
import Navbar from "../components/Navbar";

function UploadCertificate() {

  const [skill, setSkill] = useState("Python");
  const [visibility, setVisibility] = useState("private");

  // ✅ METADATA FIELDS (NEW)
  const [title, setTitle] = useState("");
  const [issuer, setIssuer] = useState("");
  const [proofLink, setProofLink] = useState("");

  const [message, setMessage] = useState("");

  async function handleUpload() {
    try {

      const token = localStorage.getItem("token");

      const response = await fetch(`${BASE_URL}/upload/certificate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
          skill_name: skill,
          visibility: visibility,

          // ✅ SEND METADATA
          metadata: {
            title: title,
            issuer: issuer,
            proof_link: proofLink
          }
        })
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage("Upload failed");
        return;
      }

      setMessage(
        `✅ Certificate uploaded for ${data.skill.skill_name}
Score: ${Math.round(data.skill.current_score)}
Visibility: ${data.skill.visibility}`
      );

      // ✅ CLEAR INPUTS
      setTitle("");
      setIssuer("");
      setProofLink("");

    } catch {
      setMessage("Server error");
    }
  }

  return (
    <>
      <Navbar />

      <div>

        <h2>Upload Certificate</h2>

        <input
          placeholder="Skill name"
          value={skill}
          onChange={(e) => setSkill(e.target.value)}
        />

        <br /><br />

        {/* ✅ METADATA INPUTS */}

        <input
          placeholder="Certificate Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <br /><br />

        <input
          placeholder="Issuer (Coursera / Udemy / Google)"
          value={issuer}
          onChange={(e) => setIssuer(e.target.value)}
        />

        <br /><br />

        <input
          placeholder="Verification / Proof Link"
          value={proofLink}
          onChange={(e) => setProofLink(e.target.value)}
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
          Upload Certificate
        </button>

        <p>{message}</p>

      </div>
    </>
  );
}

export default UploadCertificate;
