import axios from 'axios';

const API_BASE = 'http://localhost:8001/api/admin';

/**
 * Mark table as completed
 * @param {string} tableId - Table ID
 * @returns {Promise<{success: boolean}>}
 */
export const completeTable = async (tableId) => {
  const response = await axios.post(`${API_BASE}/tables/${tableId}/complete`);
  return response.data;
};
