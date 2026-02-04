const API_BASE = 'http://localhost:8001/api/customer';

/**
 * Subscribe to order status updates
 * @param {string} tableId - Table ID
 * @param {Function} onMessage - Message callback
 * @returns {EventSource} EventSource instance
 */
export const subscribeOrderStatus = (tableId, onMessage) => {
  const eventSource = new EventSource(`${API_BASE}/sse/orders/${tableId}`);
  
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onMessage(data);
  };
  
  return eventSource;
};

/**
 * Subscribe to admin order updates
 * @param {string} token - Auth token
 * @param {Function} onMessage - Message callback
 * @returns {EventSource} EventSource instance
 */
export const subscribeAdminOrders = (token, onMessage) => {
  const eventSource = new EventSource(`http://localhost:8001/api/admin/sse/orders?token=${token}`);
  
  eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onMessage(data);
  };
  
  return eventSource;
};
