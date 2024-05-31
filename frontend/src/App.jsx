// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Auth from './Auth.jsx';
import Home from './Home';
import ProductsDetail from './ProductsDetail';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Auth />} />
        <Route path="/home" element={<Home />} />
        <Route path="/product/:id" element={<ProductsDetail />} />
      </Routes>
    </Router>
  );
};
 
export default App;
