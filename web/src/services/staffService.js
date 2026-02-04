import axios from 'axios';

const API_BASE = 'http://localhost:8001/api/customer';

/**
 * Call staff to table
 * @param {string} tableId - Table ID
 * @returns {Promise<{success: boolean, callId: string}>}
 */
export const callStaff = async (tableId) => {
  const response = await axios.post(`${API_BASE}/staff-call`, { table_id: tableId });
  return response.data;
};
