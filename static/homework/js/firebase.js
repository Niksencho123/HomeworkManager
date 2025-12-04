// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.3.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.3.0/firebase-analytics.js";
import { getMessaging, getToken, onMessage } from "https://www.gstatic.com/firebasejs/12.3.0/firebase-messaging.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAZXueJvzViBFpLDw184cZWj_M28gJn8Kc",
  authDomain: "jmessaging-service.firebaseapp.com",
  projectId: "jmessaging-service",
  storageBucket: "jmessaging-service.firebasestorage.app",
  messagingSenderId: "5897662845",
  appId: "1:5897662845:web:0ebfe6ca4ad02b9b9a1c14",
  measurementId: "G-VBDL36DWJM"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);
const analytics = getAnalytics(app);

Notification.requestPermission().then((permission) => {
  if (permission === "granted") {
    console.log("Notification permission granted.");
    getToken(messaging, { vapidKey: "BJhqH4LoeaiVrQRqNIwS2s5cTao8ib8N80SlfMGXH49meT3CE4JN1NnxrshkKGO8qCf_Dh_iYjAAUxxHBLoMvy8" })
      .then((currentToken) => {
        if (currentToken) {
          console.log("Device FCM Token:", currentToken);
          // Send this token to your server and save it
        } else {
          console.log("No registration token available.");
        }
      })
      .catch((err) => {
        console.error("An error occurred while retrieving token. ", err);
      });
  }
});