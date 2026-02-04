import { createApiClient } from './apiClient';

const client = createApiClient();

/**
 * Mark table as completed
 * @param {string} tableId - Table ID
 * @returns {Promise<{success: boolean}>}
 */
export const completeTable = async (tableId) => {
  const response = await client.post(`/api/admin/tables/${tableId}/complete`);
  return response.data;
};
