// Home.js
import React from 'react';
import Navbar from './Navbar';
import Sidebar from './Sidebar';
import './Home.css';

const Home = () => {
    return (
        <div className="home-container">
            <Navbar />
            <div className="main-content">
                <Sidebar />
                <div className="content">
                    <h1>Welcome to the Home Page!</h1>
                    <p>Discover the best shoes for every occasion.</p>
                </div>
            </div>
        </div>
    );
};

export default Home;
