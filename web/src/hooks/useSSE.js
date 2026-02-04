import { useState, useEffect } from 'react';

/**
 * SSE connection hook
 * @param {string} url - SSE endpoint URL
 * @param {Function} onMessage - Message callback
 * @returns {{connected: boolean, error: Error|null}}
 */
export const useSSE = (url, onMessage) => {
  const [connected, setConnected] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!url) return;

    const eventSource = new EventSource(url);

    eventSource.onopen = () => {
      setConnected(true);
      setError(null);
    };

    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      onMessage(data);
    };

    eventSource.onerror = (err) => {
      setError(err);
      setConnected(false);
    };

    return () => {
      eventSource.close();
      setConnected(false);
    };
  }, [url, onMessage]);

  return { connected, error };
};
