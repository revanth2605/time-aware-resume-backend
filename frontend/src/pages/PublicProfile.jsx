import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { BASE_URL } from "../api/api";

function PublicProfile() {

  const { username } = useParams();
  const [profile, setProfile] = useState(null);

  useEffect(() => {

    async function loadProfile() {
      const response = await fetch(
        `${BASE_URL}/public/profile/${username}`
      );
      const data = await response.json();
      setProfile(data);
    }

    loadProfile();

  }, [username]);

  if (!profile) {
    return <p>Loading...</p>;
  }

  return (
    <div>

      <h2>{profile.username}</h2>

      <h3>Skills</h3>

      <ul>
        {profile.skills.map((skill) => (
          <li key={skill.skill_name}>
            {skill.skill_name} — {skill.current_score}
          </li>
        ))}
      </ul>

    </div>
  );
}

export default PublicProfile;
