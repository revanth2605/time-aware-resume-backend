import { useEffect, useState } from "react";
import { BASE_URL } from "../api/api";
import Navbar from "../components/Navbar";

function Dashboard() {

  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // -----------------------------
  // LOAD SKILLS
  // -----------------------------
  async function loadSkills() {
    try {
      const token = localStorage.getItem("token");

      if (!token) {
        setError("Not logged in");
        setLoading(false);
        return;
      }

      const response = await fetch(
        `${BASE_URL}/dashboard/skills`,
        {
          headers: {
            "Authorization": `Bearer ${token}`
          }
        }
      );

      const data = await response.json();

      setSkills(data.skills || []);
    }
    catch (err) {
      console.error(err);
      setError("Failed to load skills");
    }
    finally {
      setLoading(false);
    }
  }

  // -----------------------------
  // CHANGE VISIBILITY
  // -----------------------------
  async function changeVisibility(skill_name, visibility) {

    try {
      const token = localStorage.getItem("token");

      await fetch(
        `${BASE_URL}/dashboard/visibility`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
          },
          body: JSON.stringify({
            skill_name,
            visibility
          })
        }
      );

      // Reload updated skills
      loadSkills();
    }
    catch (err) {
      console.error(err);
    }
  }

  // -----------------------------
  // RUN ONCE
  // -----------------------------
  useEffect(() => {
    loadSkills();
  }, []);

  // -----------------------------
  // UI
  // -----------------------------
  return (
    <>
      <Navbar />

      <div>

        <h2>Dashboard</h2>

        {loading && <p>Loading...</p>}

        {error && <p>{error}</p>}

        {!loading && skills.length === 0 && (
          <p>No skills yet</p>
        )}

        {skills.map((skill) => (

          <div
            key={skill._id}
            style={{
              border: "1px solid gray",
              padding: "12px",
              marginBottom: "10px",
              width: "280px"
            }}
          >

            <h3
              style={{ cursor: "pointer", color: "blue" }}
              onClick={() => window.location.href = `/skill/${skill.skill_name}`}
            >
              {skill.skill_name}
            </h3>


            <p>Score: {Math.round(skill.current_score)}</p>
            <p>Certificates: {skill.certificate_count}</p>
            <p>Code Uploads: {skill.code_count}</p>

            <p>
              Visibility: <b>{skill.visibility}</b>
            </p>

            <button
              onClick={() =>
                changeVisibility(
                  skill.skill_name,
                  skill.visibility === "public"
                    ? "private"
                    : "public"
                )
              }
            >
              Make {skill.visibility === "public" ? "Private" : "Public"}
            </button>

          </div>

        ))}

      </div>
    </>
  );
}

export default Dashboard;
