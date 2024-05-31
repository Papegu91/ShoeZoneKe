import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const ProductDetail = () => {
    const { id } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/product/${id}`)
            .then(response => response.json())
            .then(data => setProduct(data));
    }, [id]);

    if (!product) {
        return <div>Loading...</div>;
    }

    return (
        <div className="product-detail">
            <h2>{product.name}</h2>
            <p><strong>Brand:</strong> {product.brand}</p>
            <p><strong>Description:</strong> {product.description}</p>
            <p><strong>Price:</strong> ${product.price}</p>
            <p><strong>Stock:</strong> {product.stock}</p>
            {product.image_url && <img src={product.image_url} alt={product.name} />}
        </div>
    );
};

export default ProductDetail;
