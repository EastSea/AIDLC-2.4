import { createApiClient } from './apiClient';

const client = createApiClient();

/**
 * Customer table login
 * @param {string} storeCode - Store code
 * @param {number} tableNumber - Table number
 * @param {string} password - Table password
 * @returns {Promise<{token: string, tableId: string, sessionId: string}>}
 */
export const loginTable = async (storeCode, tableNumber, password) => {
  const response = await client.post('/api/customer/auth/login', {
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
  const response = await client.post('/api/admin/auth/login', {
    store_code: storeCode,
    username,
    password,
  });
  return response.data;
};
