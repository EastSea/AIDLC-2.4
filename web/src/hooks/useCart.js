import { useState, useEffect } from 'react';

/**
 * Shopping cart hook
 * @returns {{items: Array, addItem: Function, removeItem: Function, updateQuantity: Function, clearCart: Function, totalAmount: number}}
 */
export const useCart = () => {
  const [items, setItems] = useState(() => {
    const saved = localStorage.getItem('cart');
    return saved ? JSON.parse(saved) : [];
  });

  useEffect(() => {
    localStorage.setItem('cart', JSON.stringify(items));
  }, [items]);

  const addItem = (menu) => {
    setItems((prev) => {
      const existing = prev.find((item) => item.id === menu.id);
      if (existing) {
        return prev.map((item) =>
          item.id === menu.id ? { ...item, quantity: item.quantity + 1 } : item
        );
      }
      return [...prev, { ...menu, quantity: 1 }];
    });
  };

  const removeItem = (menuId) => {
    setItems((prev) => prev.filter((item) => item.id !== menuId));
  };

  const updateQuantity = (menuId, quantity) => {
    if (quantity === 0) {
      removeItem(menuId);
    } else {
      setItems((prev) =>
        prev.map((item) => (item.id === menuId ? { ...item, quantity } : item))
      );
    }
  };

  const clearCart = () => {
    setItems([]);
  };

  const totalAmount = items.reduce((sum, item) => sum + item.price * item.quantity, 0);

  return { items, addItem, removeItem, updateQuantity, clearCart, totalAmount };
};
