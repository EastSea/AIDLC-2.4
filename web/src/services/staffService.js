import axios from 'axios';

const API_BASE = `${process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'}/api/customer`;

/**
 * Call staff to table
 * @param {string} tableId - Table ID
 * @returns {Promise<{success: boolean, callId: string}>}
 */
export const callStaff = async (tableId) => {
  const response = await axios.post(`${API_BASE}/staff-call`, { table_id: tableId });
  return response.data;
};
