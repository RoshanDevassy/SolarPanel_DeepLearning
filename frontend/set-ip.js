const os = require("os");
const fs = require("fs");
const path = require("path");

// Function to get the active IP (WiFi or Ethernet)
function getActiveIP() {
  const interfaces = os.networkInterfaces();
  let selectedIP = "127.0.0.1"; // Default fallback

  for (const name of Object.keys(interfaces)) {
    for (const net of interfaces[name]) {
      if (net.family === "IPv4" && !net.internal) {
        // Prioritize WiFi (192.168.x.x), otherwise use Ethernet
        if (net.address.startsWith("192.168") || net.address.startsWith("10.")) {
          selectedIP = net.address;
        }
      }
    }
  }
  return selectedIP;
}

// Get active network IP
const activeIP = getActiveIP();
const envContent = `NEXT_PUBLIC_API_BASE_URL=http://${activeIP}:8000\n`;

// Save to `.env.local`
fs.writeFileSync(path.join(__dirname, ".env.local"), envContent);
console.log(`✅ .env.local updated with Active IP: ${activeIP}`);
