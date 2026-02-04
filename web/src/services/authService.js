import axios from 'axios';

const API_BASE = 'http://localhost:8001/api/customer';

/**
 * Customer table login
 * @param {string} storeCode - Store code
 * @param {number} tableNumber - Table number
 * @param {string} password - Table password
 * @returns {Promise<{token: string, tableId: string, sessionId: string}>}
 */
export const loginTable = async (storeCode, tableNumber, password) => {
  const response = await axios.post(`${API_BASE}/auth/login`, {
    store_code: storeCode,
    table_number: tableNumber,
    password,
  });
  return response.data;
};

/**
 * Admin login
 * @param {string} storeCode - Store code
 * @param {string} username - Admin username
 * @param {string} password - Admin password
 * @returns {Promise<{token: string, storeId: string, userId: string}>}
 */
export const loginAdmin = async (storeCode, username, password) => {
  const response = await axios.post('http://localhost:8001/api/admin/auth/login', {
    store_code: storeCode,
    username,
    password,
  });
  return response.data;
};
