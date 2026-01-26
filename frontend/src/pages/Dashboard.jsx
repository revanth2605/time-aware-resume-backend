import { useEffect, useState } from "react";
import { BASE_URL } from "../api/api";
import Navbar from "../components/Navbar";

function Dashboard() {

  const [data, setData] = useState(null);

  useEffect(() => {

    async function loadDashboard() {

      const token = localStorage.getItem("token");

      const response = await fetch(`${BASE_URL}/dashboard/get`, {
        method: "GET",
        headers: {
          "Authorization": `Bearer ${token}`
        }
      });

      const result = await response.json();
      setData(result);
    }

    loadDashboard();

  }, []);

  if (!data) return <p>Loading...</p>;

  if (data.message) return <p>{data.message}</p>;

  const skill = data.skill;

  return (
    <>
      <Navbar />

      <div>

        <h2>Dashboard</h2>

        <div style={{
          border: "1px solid gray",
          padding: "15px",
          width: "250px"
        }}>

          <h3>{skill.skill_name}</h3>

          <p>Score: {skill.current_score}</p>
          <p>Certificates: {skill.certificate_count}</p>
          <p>Code Uploads: {skill.code_count}</p>
          <p>Visibility: {skill.visibility}</p>

        </div>

      </div>
    </>
  );
}

export default Dashboard;
