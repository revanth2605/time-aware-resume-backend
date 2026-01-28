import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { BASE_URL } from "../api/api";
import Navbar from "../components/Navbar";

function CodeHistory() {

  const { skill } = useParams();
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(true);

  // -------------------------
  // LOAD HISTORY
  // -------------------------
  useEffect(() => {

    async function loadHistory() {

      try {
        const token = localStorage.getItem("token");

        const res = await fetch(
          `${BASE_URL}/evidence/code/${skill}`,
          {
            headers: {
              Authorization: `Bearer ${token}`
            }
          }
        );

        const data = await res.json();
        setRecords(data.records || []);
      }
      catch (err) {
        console.error(err);
      }
      finally {
        setLoading(false);
      }

    }

    loadHistory();

  }, [skill]);

  // -------------------------
  // DELETE RECORD
  // -------------------------
  async function deleteRecord(id) {

    try {
      const token = localStorage.getItem("token");

      await fetch(
        `${BASE_URL}/evidence/code/${id}`,
        {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      setRecords(records.filter(r => r._id !== id));
    }
    catch (err) {
      console.error(err);
    }
  }

  // -------------------------
  // UI
  // -------------------------
  return (
    <>
      <Navbar />

      <h2>Code History – {skill}</h2>

      {loading && <p>Loading...</p>}

      {!loading && records.length === 0 && (
        <p>No records</p>
      )}

      {records.map(r => (
        <div
          key={r._id}
          style={{
            border: "1px solid gray",
            padding: "10px",
            marginBottom: "8px"
          }}
        >

          <b>{r.metadata?.title || "Untitled Project"}</b>

          {r.metadata?.description && (
            <p>{r.metadata.description}</p>
          )}

          {r.metadata?.repo_link && (
            <a href={r.metadata.repo_link} target="_blank">
              View Repository
            </a>
          )}

          <p>
            Date: {new Date(r.created_at).toLocaleString()}
          </p>

          <button onClick={() => deleteRecord(r._id)}>
            Delete
          </button>

        </div>
      ))}

    </>
  );
}

export default CodeHistory;
