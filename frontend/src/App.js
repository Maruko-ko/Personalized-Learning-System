import React from 'react';
import './App.css';
import LoginPage from './pages/LoginPage';
import Footer from './components/Footer';
import UserInput from './pages/UserInput';

function App() {
  return (
    <div className ="login-container">
      <div className="App">
        <LoginPage />
      </div>
      <Footer />
    </div>
  );
}

export default App;
