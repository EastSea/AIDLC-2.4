import { createApiClient } from './apiClient';

const client = createApiClient();

/**
 * Fetch orders for admin
 * @param {string} [tableId] - Optional table filter
 * @returns {Promise<Array>} Order array
 */
export const getAdminOrders = async (tableId) => {
  const params = tableId ? { table_id: tableId } : {};
  const response = await client.get('/api/admin/orders', { params });
  return response.data;
};

/**
 * Update order status
 * @param {string} orderId - Order ID
 * @param {string} status - New status (pending|preparing|completed)
 * @returns {Promise<{success: boolean}>}
 */
export const updateOrderStatus = async (orderId, status) => {
  const response = await client.patch(`/api/admin/orders/${orderId}/status`, { status });
  return response.data;
};

/**
 * Delete order
 * @param {string} orderId - Order ID
 * @returns {Promise<{success: boolean}>}
 */
export const deleteOrder = async (orderId) => {
  const response = await client.delete(`/api/admin/orders/${orderId}`);
  return response.data;
};
