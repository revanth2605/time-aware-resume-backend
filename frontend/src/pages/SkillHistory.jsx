import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { BASE_URL } from "../api/api";
import Navbar from "../components/Navbar";

function SkillHistory() {

  const { skillName } = useParams();

  const [codeRecords, setCodeRecords] = useState([]);
  const [certRecords, setCertRecords] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    async function loadHistory() {

      const token = localStorage.getItem("token");

      const codeRes = await fetch(
        `${BASE_URL}/evidence/code/${skillName}`,
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      const certRes = await fetch(
        `${BASE_URL}/evidence/certificate/${skillName}`,
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      const codeData = await codeRes.json();
      const certData = await certRes.json();

      setCodeRecords(codeData.records || []);
      setCertRecords(certData.records || []);
      setLoading(false);
    }

    loadHistory();

  }, [skillName]);

  return (
    <>
      <Navbar />

      <div style={{ padding: "20px" }}>

        <h2>{skillName} History</h2>

        {loading && <p>Loading...</p>}

        {!loading && (
          <>

            <h3>💻 Code Uploads</h3>

            {codeRecords.length === 0 && <p>No code evidence</p>}

            {codeRecords.map((item) => (
              <div key={item._id}
                   style={{ border: "1px solid #ccc", padding: "8px", marginBottom: "6px" }}>
                <p>Uploaded: {new Date(item.created_at).toLocaleString()}</p>
              </div>
            ))}

            <h3>📜 Certificates</h3>

            {certRecords.length === 0 && <p>No certificates</p>}

            {certRecords.map((item) => (
              <div key={item._id}
                   style={{ border: "1px solid #ccc", padding: "8px", marginBottom: "6px" }}>
                <p>Uploaded: {new Date(item.created_at).toLocaleString()}</p>
              </div>
            ))}

          </>
        )}

      </div>
    </>
  );
}

export default SkillHistory;
