import { useState, useEffect } from 'react';

/**
 * Authentication hook
 * @returns {{isAuthenticated: boolean, user: Object|null, login: Function, logout: Function}}
 */
export const useAuth = () => {
  const [user, setUser] = useState(() => {
    const tableAuth = localStorage.getItem('tableAuth');
    const adminAuth = localStorage.getItem('adminAuth');
    return tableAuth ? JSON.parse(tableAuth) : adminAuth ? JSON.parse(adminAuth) : null;
  });

  const login = (authData, type = 'table') => {
    const key = type === 'admin' ? 'adminAuth' : 'tableAuth';
    localStorage.setItem(key, JSON.stringify(authData));
    setUser(authData);
  };

  const logout = () => {
    localStorage.removeItem('tableAuth');
    localStorage.removeItem('adminAuth');
    setUser(null);
  };

  return {
    isAuthenticated: !!user,
    user,
    login,
    logout,
  };
};
