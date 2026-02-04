import axios from 'axios';

const API_BASE = `${process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'}/api/admin`;

/**
 * Fetch orders for admin
 * @param {string} [tableId] - Optional table filter
 * @returns {Promise<Array>} Order array
 */
export const getAdminOrders = async (tableId) => {
  const params = tableId ? { table_id: tableId } : {};
  const response = await axios.get(`${API_BASE}/orders`, { params });
  return response.data;
};

/**
 * Update order status
 * @param {string} orderId - Order ID
 * @param {string} status - New status (pending|preparing|completed)
 * @returns {Promise<{success: boolean}>}
 */
export const updateOrderStatus = async (orderId, status) => {
  const response = await axios.patch(`${API_BASE}/orders/${orderId}/status`, { status });
  return response.data;
};

/**
 * Delete order
 * @param {string} orderId - Order ID
 * @returns {Promise<{success: boolean}>}
 */
export const deleteOrder = async (orderId) => {
  const response = await axios.delete(`${API_BASE}/orders/${orderId}`);
  return response.data;
};
