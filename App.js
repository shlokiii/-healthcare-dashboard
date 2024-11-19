import React, { useState } from "react";
import "./App.css";
import { FaUser, FaFileUpload, FaBirthdayCake } from "react-icons/fa";

const App = () => {
  const [formData, setFormData] = useState({
    name: "",
    age: "Select Age",
    file: null,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleFileUpload = (e) => {
    setFormData((prev) => ({ ...prev, file: e.target.files[0] }));
  };

  const handleSubmit = () => {
    const { name, age, file } = formData;

    // Validate all fields
    if (!name || age === "Select Age" || !file) {
      alert("Please fill all fields and upload a file.");
      return;
    }

    alert(
      `Submitted:\nName: ${name}\nAge: ${age}\nFile: ${file.name}`
    );
  };

  // Generate age options from 1 to 120
  const ageOptions = Array.from({ length: 120 }, (_, i) => i + 1);

  return (
    <div className="dashboard">
      <header className="header">
        <h1>Healthcare Dashboard</h1>
      </header>
      <div className="card">
        <h2>Patient Information</h2>
        <form className="form">
          <div className="form-group">
            <label>
              <FaUser /> Name:
            </label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter your name"
            />
          </div>
          <div className="form-group">
            <label>
              <FaBirthdayCake /> Age:
            </label>
            <select
              name="age"
              value={formData.age}
              onChange={handleChange}
            >
              <option value="Select Age">Select Age</option>
              {ageOptions.map((age) => (
                <option key={age} value={age}>
                  {age}
                </option>
              ))}
            </select>
          </div>
          <div className="form-group">
            <label>
              <FaFileUpload /> Upload File:
            </label>
            <input type="file" onChange={handleFileUpload} />
          </div>
          <button type="button" onClick={handleSubmit}>
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

export default App;