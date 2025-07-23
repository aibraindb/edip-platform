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
