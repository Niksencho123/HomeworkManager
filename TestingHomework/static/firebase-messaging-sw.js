// Import the Firebase scripts that the service worker needs
importScripts("https://www.gstatic.com/firebasejs/12.3.0/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/12.3.0/firebase-messaging.js");

// Initialize Firebase inside the service worker
firebase.initializeApp({
  apiKey: "AIzaSyAZXueJvzViBFpLDw184cZWj_M28gJn8Kc",
  authDomain: "jmessaging-service.firebaseapp.com",
  projectId: "jmessaging-service",
  storageBucket: "jmessaging-service.firebasestorage.app",
  messagingSenderId: "5897662845",
  appId: "1:5897662845:web:0ebfe6ca4ad02b9b9a1c14",
  measurementId: "G-VBDL36DWJM"
});

// Retrieve an instance of Firebase Messaging
const messaging = firebase.messaging();