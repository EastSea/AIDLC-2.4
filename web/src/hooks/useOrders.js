import { useState, useEffect } from 'react';
import { getOrders } from '../services/orderService';

/**
 * Order history hook
 * @param {string} sessionId - Session ID
 * @returns {{orders: Array, loading: boolean, error: Error|null, refetch: Function}}
 */
export const useOrders = (sessionId) => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchOrders = async () => {
    if (!sessionId) return;
    
    setLoading(true);
    setError(null);
    try {
      const data = await getOrders(sessionId);
      setOrders(data);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, [sessionId]);

  return { orders, loading, error, refetch: fetchOrders };
};
