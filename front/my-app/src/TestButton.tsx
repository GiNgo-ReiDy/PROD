import React from "react";

export default function TestButton() {
  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        console.log("submit fired!");
        alert("Submit работает");
      }}
    >
      <button type="submit">Проверка</button>
    </form>
  );
}
