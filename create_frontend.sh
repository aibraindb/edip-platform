#!/bin/bash
set -e

echo "🎨 Bootstrapping React frontend..."

# Step 1: Scaffold Vite + React
npm create vite@latest edip-frontend -- --template react
cd edip-frontend

# Step 2: Install deps
npm install axios

# Step 3: Create src/components and utility folders
mkdir -p src/components src/api

# Step 4: Create UploadForm component
cat << 'EOF' > src/components/UploadForm.jsx
import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      setStatus("Uploading...");
      const res = await axios.post("http://localhost:8080/upload", formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setStatus(`Uploaded: ${res.data}`);
    } catch (err) {
      console.error(err);
      setStatus("Upload failed.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button type="submit">Upload</button>
      <p>{status}</p>
    </form>
  );
}

export default UploadForm;
EOF

# Step 5: Replace App.jsx
cat << 'EOF' > src/App.jsx
import React from 'react';
import UploadForm from './components/UploadForm';

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>EDIP Document Upload</h1>
      <UploadForm />
    </div>
  );
}

export default App;
EOF

echo "✅ React frontend initialized in edip-frontend/"
echo "👉 Run it with:"
echo "cd edip-frontend"
echo "npm install && npm run dev"
