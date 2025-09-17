import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import LoginPage from './pages/LoginPage';
import Footer from './components/Footer';
import UserInput from './pages/UserInput';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/user-input" element={<UserInput />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}
export default App;
