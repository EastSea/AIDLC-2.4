import React from 'react';

/**
 * Menu card component
 * @param {Object} props
 * @param {Object} props.menu - Menu data
 * @param {Function} props.onAddToCart - Add to cart callback
 */
const MenuCard = ({ menu, onAddToCart }) => {
  return (
    <div className="menu-card">
      {menu.imageUrl && <img src={menu.imageUrl} alt={menu.name} />}
      <h3>{menu.name}</h3>
      <p className="price">{menu.price.toLocaleString()}원</p>
      {menu.servingSize && <p className="serving-size">{menu.servingSize}</p>}
      <button onClick={() => onAddToCart(menu)}>장바구니 담기</button>
    </div>
  );
};

export default MenuCard;
