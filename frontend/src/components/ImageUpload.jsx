"use client";

import { useState } from "react";
import Image from "next/image";

export default function ImageUploader() {
  const BASE_URL =
    process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";
  console.log("Using API base URL:", BASE_URL);
  console.log(
    "NEXT_PUBLIC_API_BASE_URL:",
    process.env.NEXT_PUBLIC_API_BASE_URL
  );
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [panelPrediction, setPanelPrediction] = useState(null);
  const [faultPrediction, setFaultPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Handle file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (!file) return;

    setImage(file);
    setPreview(URL.createObjectURL(file)); // Show image preview
    setPanelPrediction(null);
    setFaultPrediction(null);
    setError(null);
  };

  // Upload image to FastAPI for Solar Panel Detection
  const handleUpload = async () => {
    if (!image) {
      alert("⚠️Please select an image first!");
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append("file", image);

    try {
      // Step 1: Check if the image contains a solar panel
      const panelResponse = await fetch(`${BASE_URL}/detect-panel/`, {
        method: "POST",
        body: formData,
      });

      if (!panelResponse.ok) throw new Error("❌ Failed to detect solar panel");

      const panelData = await panelResponse.json();
      setPanelPrediction(panelData);

      if (panelData.predicted_class === "No Solar Panel Detected") {
        setFaultPrediction(null);
        return;
      }

      // Step 2: If solar panel detected, check for faults
      const faultResponse = await fetch(`${BASE_URL}/detect-fault/`, {
        method: "POST",
        body: formData,
      });

      if (!faultResponse.ok) throw new Error("❌ Failed to detect fault");

      const faultData = await faultResponse.json();
      setFaultPrediction(faultData);
    } catch (error) {
      console.error("Error:", error);
      setError("❌ Failed to process the image. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center gap-5 p-5">
      <h1 className="text-2xl font-bold">Solar Panel Fault Detection</h1>

      {/* File Upload */}
      <input
        type="file"
        onChange={handleFileChange}
        accept="image/jpeg, image/jpg, image/png"
        className="border p-2 rounded-md"
      />

      {/* Image Preview */}
      {preview && (
        <img
          src={preview}
          alt="Preview"
          className="rounded-lg shadow-md w-72 h-72 object-cover"
        />
      )}

      {/* Upload & Predict Button */}
      <button
        onClick={handleUpload}
        disabled={loading}
        className={`flex gap-2 px-4 py-2 text-white font-semibold rounded-md transition ${
          loading
            ? "bg-gray-400 cursor-not-allowed"
            : "bg-blue-500 hover:bg-blue-600"
        }`}
      >
          {loading ? <span className=" animate-spin duration-75"><Image src="/icons/processing_icon.svg" height={25} width={25} alt="processing_icon"/></span> : ''}
        {loading ? "Processing..." : "⬆️ Upload & Predict"}
      </button>

      {/* Error Message */}
      {error && <p className="text-red-500">{error}</p>}

      {/* Prediction Results */}
      {panelPrediction && (
        <div className="text-lg font-medium dark:text-white mt-3">
          <h3>Panel Detection: {panelPrediction.predicted_class}</h3>
          <p>
            Confidence:{" "}
            {panelPrediction.confidence !== undefined &&
            panelPrediction.confidence !== null
              ? `${(panelPrediction.confidence * 100).toFixed(2)}%`
              : "N/A"}
          </p>
        </div>
      )}

      {faultPrediction && (
        <div className="text-lg font-medium dark:text-white mt-3">
          <h3>Detected: {faultPrediction.predicted_fault}</h3>
          <p>
            Confidence:{" "}
            {faultPrediction.confidence !== undefined
              ? `${(faultPrediction.confidence * 100).toFixed(2)}%`
              : "N/A"}
          </p>
        </div>
      )}
    </div>
  );
}

/* 'use client'

import { useState } from "react";

export default function ImageUploader() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  // Handle file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file)); // Show image preview
  };

  // Upload image to FastAPI
  const handleUpload = async () => {
    if (!image) {
      alert("Please select an image first!");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error("Error uploading image:", error);
      alert("Failed to get prediction");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2>Solar Panel Fault Detection</h2>

      <input type="file" onChange={handleFileChange} accept="image/jpeg, image/jpg, image/png" />
      {preview && <img src={preview} alt="Preview" className="preview" />}

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Predict"}
      </button>

      {prediction && (
        <div className="result">
          <h3>Prediction: {prediction.predicted_class}</h3>
          <p>Confidence: {(prediction.confidence * 100).toFixed(2)}%</p>
        </div>
      )}

      <style jsx>{`
        .container { text-align: center; margin: 20px; }
        .preview { width: 300px; margin-top: 10px; }
        .result { margin-top: 20px; font-size: 18px; }
        button { margin-top: 10px; padding: 10px 20px; cursor: pointer; }
      `}</style>
    </div>
  );
}

 */
