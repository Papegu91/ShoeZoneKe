// src/Home.jsx
import React from 'react';
import Navbar from './Navbar';
import Sidebar from './Sidebar';
import Products from './Products';
import './Home.css';
import ProductsDetail from './ProductsDetail';


const Home = () => {
    return (
        <div className="home-container">
            <Navbar />
            <div className="main-content">
                <Sidebar />
                <div className="content">
                    <h1>Welcome to the Home Page!</h1>
                    <p>Discover the best shoes for every occasion.</p>
                    <Products />
                </div>
            </div>
        </div>
    );
};

export default Home;

