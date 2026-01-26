import { useState } from "react";
import { BASE_URL } from "../api/api";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

function SearchUser() {

  const [username, setUsername] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function handleSearch() {

    setError("");
    setResult(null);

    const response = await fetch(`${BASE_URL}/users/public`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: username
      })
    });

    const data = await response.json();

    if (data.error) {
      setError(data.error);
    } else {
      setResult(data);
    }
  }

  return (
    <>
      <Navbar />

      <div>

        <h2>Search User</h2>

        <input
          placeholder="Enter username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <br /><br />

        <button onClick={handleSearch}>
          Search
        </button>

        <br /><br />

        {error && <p>{error}</p>}

        {result && (
          <div>
            <p><b>{result.username}</b></p>

            <Link to={`/profile/${result.username}`}>
              View Profile
            </Link>
          </div>
        )}

      </div>
    </>
  );
}

export default SearchUser;
