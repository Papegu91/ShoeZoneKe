// Sidebar.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
    return (
        <div className="sidebar">
            <ul>
                <li><Link to="/men">Men's Shoes</Link></li>
                <li><Link to="/women">Women's Shoes</Link></li>
                <li><Link to="/kids">Kids' Shoes</Link></li>
                <li><Link to="/sale">Sale</Link></li>
            </ul>
        </div>
    );
};

export default Sidebar;
