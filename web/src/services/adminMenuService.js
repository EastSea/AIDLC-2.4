import axios from 'axios';

const API_BASE = `${process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'}/api/admin`;

/**
 * Fetch all menus for admin
 * @returns {Promise<Array>} Menu array
 */
export const getAdminMenus = async () => {
  const response = await axios.get(`${API_BASE}/menus`);
  return response.data;
};

/**
 * Create new menu
 * @param {Object} menuData - Menu data
 * @returns {Promise<Object>} Created menu
 */
export const createMenu = async (menuData) => {
  const response = await axios.post(`${API_BASE}/menus`, menuData);
  return response.data;
};

/**
 * Update menu
 * @param {string} menuId - Menu ID
 * @param {Object} menuData - Updated menu data
 * @returns {Promise<Object>} Updated menu
 */
export const updateMenu = async (menuId, menuData) => {
  const response = await axios.put(`${API_BASE}/menus/${menuId}`, menuData);
  return response.data;
};

/**
 * Delete menu
 * @param {string} menuId - Menu ID
 * @returns {Promise<{success: boolean}>}
 */
export const deleteMenu = async (menuId) => {
  const response = await axios.delete(`${API_BASE}/menus/${menuId}`);
  return response.data;
};
