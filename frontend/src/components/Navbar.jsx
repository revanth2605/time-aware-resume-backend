import { Link, useNavigate } from "react-router-dom";

function Navbar() {

  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  function handleLogout() {
    localStorage.removeItem("token");
    navigate("/");
  }

  return (
    <div style={{ padding: "10px", background: "#eee" }}>

      {/* ALWAYS VISIBLE */}
      <Link to="/search">Search</Link> |{" "}

      {token ? (
        <>
          <Link to="/dashboard">Dashboard</Link> |{" "}
          <Link to="/upload-code">Upload Code</Link> |{" "}
          <Link to="/upload-certificate">Upload Certificate</Link> |{" "}
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <>
          <Link to="/">Login</Link> |{" "}
          <Link to="/register">Register</Link>
        </>
      )}

    </div>
  );
}

export default Navbar;
