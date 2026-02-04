import { createApiClient } from './apiClient';

const client = createApiClient();

/**
 * Fetch all menus for admin
 * @returns {Promise<Array>} Menu array
 */
export const getAdminMenus = async () => {
  const response = await client.get('/api/admin/menus');
  return response.data;
};

/**
 * Create new menu
 * @param {Object} menuData - Menu data
 * @returns {Promise<Object>} Created menu
 */
export const createMenu = async (menuData) => {
  const response = await client.post('/api/admin/menus', menuData);
  return response.data;
};

/**
 * Update menu
 * @param {string} menuId - Menu ID
 * @param {Object} menuData - Updated menu data
 * @returns {Promise<Object>} Updated menu
 */
export const updateMenu = async (menuId, menuData) => {
  const response = await client.put(`/api/admin/menus/${menuId}`, menuData);
  return response.data;
};

/**
 * Delete menu
 * @param {string} menuId - Menu ID
 * @returns {Promise<{success: boolean}>}
 */
export const deleteMenu = async (menuId) => {
  const response = await client.delete(`/api/admin/menus/${menuId}`);
  return response.data;
};
