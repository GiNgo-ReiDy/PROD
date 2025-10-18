import React, { useState } from "react";

export default function LoginForm() {
  const [username, setUsername] = useState("200");
  const [password, setPassword] = useState("200");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
  e.preventDefault();
  setMessage("");
  setLoading(true);

  try {
    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    const res = await fetch("http://127.0.0.1:8000/api/auth/test", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formData.toString(),
    });

    if (!res.ok) {
      throw new Error(await res.text());
    }

    const data = await res.json();
    setMessage("Успешно! Сервер вернул: " + JSON.stringify(data));

    if (data.access_token) localStorage.setItem("token", data.access_token);
  } catch (err: any) {
    setMessage("Ошибка: " + err.message);
  } finally {
    setLoading(false);
  }
};


  return (
    <div style={{ marginTop: "100px", textAlign: "center" }}>
      <form onSubmit={handleSubmit} style={{ display: "inline-block" }}>
        <button type="submit" disabled={loading} style={{ padding: "10px 20px" }}>
          {loading ? "Отправка..." : "Войти"}
        </button>
      </form>

      {message && <div style={{ marginTop: "20px" }}>{message}</div>}
    </div>
  );
}
