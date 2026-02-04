import axios from 'axios';

const API_BASE = `${process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'}/api/customer`;

/**
 * Create new order
 * @param {string} sessionId - Session ID
 * @param {Array<{menuId: string, quantity: number}>} items - Order items
 * @returns {Promise<{orderId: string, orderNumber: string}>}
 */
export const createOrder = async (sessionId, items) => {
  const response = await axios.post(`${API_BASE}/orders`, { 
    session_id: sessionId, 
    items: items.map(item => ({ menu_id: item.menuId, quantity: item.quantity }))
  });
  return response.data;
};

/**
 * Fetch order history
 * @param {string} sessionId - Session ID
 * @returns {Promise<Array>} Order array
 */
export const getOrders = async (sessionId) => {
  const response = await axios.get(`${API_BASE}/orders`, {
    params: { session_id: sessionId }
  });
  return response.data;
};
