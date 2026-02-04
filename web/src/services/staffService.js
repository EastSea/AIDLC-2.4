import { createApiClient } from './apiClient';

const client = createApiClient();

/**
 * Call staff to table
 * @param {string} tableId - Table ID
 * @returns {Promise<{success: boolean, callId: string}>}
 */
export const callStaff = async (tableId) => {
  const response = await client.post('/api/customer/staff-call', { table_id: tableId });
  return response.data;
};
