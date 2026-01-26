import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import UploadCode from "./pages/UploadCode";
import UploadCertificate from "./pages/UploadCertificate";
import PublicProfile from "./pages/PublicProfile";
import SearchUser from "./pages/SearchUser";
import Register from "./pages/Register";

import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Login />} />
        <Route path="/profile/:username" element={<PublicProfile />} />
        <Route path="/search" element={<SearchUser />} />
        <Route path="/register" element={<Register />} />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/upload-code"
          element={
            <ProtectedRoute>
              <UploadCode />
            </ProtectedRoute>
          }
        />

        <Route
          path="/upload-certificate"
          element={
            <ProtectedRoute>
              <UploadCertificate />
            </ProtectedRoute>
          }
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
