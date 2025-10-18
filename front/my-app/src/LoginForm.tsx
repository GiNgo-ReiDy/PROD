import React, { useState } from "react";

const API_URL = "http://127.0.0.1:8000/api";

export default function AdminTestPanel() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [result, setResult] = useState<any>(null);

  const [groupName, setGroupName] = useState("");
  const [groupId, setGroupId] = useState<number | null>(null);

  const [userUuid, setUserUuid] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [groupForUser, setGroupForUser] = useState<number | null>(null);

  const token = localStorage.getItem("token"); // используем токен, полученный при логине

  async function apiCall(
    method: string,
    endpoint: string,
    body?: object
  ): Promise<void> {
    setLoading(true);
    setMessage("");
    setResult(null);

    try {
      const res = await fetch(`${API_URL}${endpoint}`, {
        method,
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: body ? JSON.stringify(body) : undefined,
      });

      if (res.status === 204) {
        setMessage("Нет данных (204 No Content)");
        setResult(null);
        return;
      }

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(`${res.status}: ${JSON.stringify(data)}`);

      setMessage(`✅ Успешно (${res.status})`);
      setResult(data);
    } catch (err: any) {
      setMessage("❌ Ошибка: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ padding: "20px", fontFamily: "monospace" }}>
      <h2>🧩 Admin Test Panel</h2>
      <p>Тестирование CRUD-эндпоинтов /groups и /users</p>

      <hr />

      {/* GROUPS */}
      <h3>📦 Groups</h3>
      <button onClick={() => apiCall("GET", "/groups/")} disabled={loading}>
        GET /groups
      </button>

      <div>
        <input
          placeholder="Название группы"
          value={groupName}
          onChange={(e) => setGroupName(e.target.value)}
        />
        <button
          onClick={() => apiCall("POST", "/groups/", { name: groupName })}
          disabled={loading}
        >
          POST /groups
        </button>
      </div>

      <div>
        <input
          type="number"
          placeholder="ID группы"
          value={groupId ?? ""}
          onChange={(e) => setGroupId(Number(e.target.value))}
        />
        <button
          onClick={() =>
            apiCall("PATCH", "/groups/", { id: groupId, name: groupName })
          }
          disabled={loading}
        >
          PATCH /groups
        </button>
        <button
          onClick={() => apiCall("DELETE", "/groups/", { id: groupId })}
          disabled={loading}
        >
          DELETE /groups
        </button>
      </div>

      <hr />

      {/* USERS */}
      <h3>👤 Users</h3>
      <button onClick={() => apiCall("GET", "/users/")} disabled={loading}>
        GET /users
      </button>

      <div>
        <input
          placeholder="Имя пользователя"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          placeholder="Пароль"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <input
          type="number"
          placeholder="Group ID"
          value={groupForUser ?? ""}
          onChange={(e) => setGroupForUser(Number(e.target.value))}
        />
        <button
          onClick={() =>
            apiCall("POST", "/users/", {
              username,
              password,
              group_id: groupForUser,
            })
          }
          disabled={loading}
        >
          POST /users
        </button>
      </div>

      <div>
        <input
          placeholder="UUID пользователя"
          value={userUuid}
          onChange={(e) => setUserUuid(e.target.value)}
        />
        <button
          onClick={() =>
            apiCall("PATCH", "/users/", {
              uuid: userUuid,
              username,
              group_id: groupForUser,
            })
          }
          disabled={loading}
        >
          PATCH /users
        </button>
        <button
          onClick={() => apiCall("DELETE", "/users/", { uuid: userUuid })}
          disabled={loading}
        >
          DELETE /users
        </button>
      </div>

      <hr />

      {/* RESULTS */}
      {loading && <p>⏳ Выполнение запроса...</p>}
      {message && <p>{message}</p>}
      {result && (
        <pre
          style={{
            textAlign: "left",
            background: "#f3f3f3",
            padding: "10px",
            borderRadius: "6px",
            marginTop: "10px",
          }}
        >
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}
