import axios from 'axios';

const API_BASE = `${process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'}/api/admin`;

/**
 * Mark table as completed
 * @param {string} tableId - Table ID
 * @returns {Promise<{success: boolean}>}
 */
export const completeTable = async (tableId) => {
  const response = await axios.post(`${API_BASE}/tables/${tableId}/complete`);
  return response.data;
};
