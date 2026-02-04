import axios from 'axios';

const API_BASE = 'http://localhost:8001/api/customer';

/**
 * Fetch all categories
 * @returns {Promise<Array>} Category array
 */
export const getCategories = async () => {
  const response = await axios.get(`${API_BASE}/categories`);
  return response.data;
};

/**
 * Fetch menus with filters
 * @param {string} [categoryId] - Optional category filter
 * @param {string} [servingSize] - Optional serving size filter
 * @returns {Promise<Array>} Menu array
 */
export const getMenus = async (categoryId, servingSize) => {
  const params = {};
  if (categoryId) params.category_id = categoryId;
  if (servingSize) params.serving_size = servingSize;
  
  const response = await axios.get(`${API_BASE}/menus`, { params });
  return response.data;
};

/**
 * Fetch menu details
 * @param {string} menuId - Menu ID
 * @returns {Promise<Object>} Menu object
 */
export const getMenuDetail = async (menuId) => {
  const response = await axios.get(`${API_BASE}/menus/${menuId}`);
  return response.data;
};
