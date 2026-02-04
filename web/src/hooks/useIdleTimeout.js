import { useEffect, useRef } from 'react';

/**
 * Idle timeout hook
 * @param {number} timeoutMs - Timeout in milliseconds
 * @param {Function} onTimeout - Timeout callback
 */
export const useIdleTimeout = (timeoutMs, onTimeout) => {
  const timeoutRef = useRef(null);

  const resetTimeout = () => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    timeoutRef.current = setTimeout(onTimeout, timeoutMs);
  };

  useEffect(() => {
    const events = ['mousedown', 'keydown', 'scroll', 'touchstart'];

    events.forEach((event) => {
      window.addEventListener(event, resetTimeout);
    });

    resetTimeout();

    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
      events.forEach((event) => {
        window.removeEventListener(event, resetTimeout);
      });
    };
  }, [timeoutMs, onTimeout]);
};
