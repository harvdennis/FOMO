import './App.css';
import Nav from './components/Nav';
import Home from './pages/Home';
import Calendar from './pages/Calendar';
import Deadlines from './pages/Deadlines';
import About from './pages/About';
import Profile from './pages/Profile';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';

function App() {
  const theme = useSelector((state) => state.theme.value);
  document.body.setAttribute('data-theme', theme)

  return (
    <Router>
      <Nav />
      <div data-theme={theme} className='bodyOverride'>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Calendar" element={<Calendar />} />
          <Route path="/Deadlines" element={<Deadlines />} />
          <Route path="/About" element={<About />} />
          <Route path="/Profile" element={<Profile />} />
        </Routes>
      </div>
    </Router>

  );
}

export default App;
