import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './Products.css';

const Products = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/products')
            .then(response => response.json())
            .then(data => setProducts(data));
    }, []);

    return (
        <div className="products">
            <h2>Products</h2>
            <div className="product-grid">
                {products.map(product => (
                    <div key={product.id} className="product-card">
                        <img src={product.image_url} alt={product.name} className="product-image" />
                        <div className="product-info">
                            <h3><Link to={`/product/${product.id}`}>{product.name}</Link></h3>
                            <p>{product.brand}</p>
                            <p>{product.description}</p>
                            <p>${product.price.toFixed(2)}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Products;
