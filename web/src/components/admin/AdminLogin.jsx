import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginAdmin } from '../../services/authService';
import { useAuth } from '../../hooks/useAuth';

/**
 * Admin login component
 */
const AdminLogin = () => {
  const [storeCode, setStoreCode] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const data = await loginAdmin(storeCode, username, password);
      login({
        token: data.token,
        storeId: data.store_id,
        userId: data.user_id
      }, 'admin');
      navigate('/admin/dashboard');
    } catch (err) {
      setError(err.response?.data?.message || '로그인 실패');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="admin-login">
      <h2>관리자 로그인</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="매장 코드"
          value={storeCode}
          onChange={(e) => setStoreCode(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="사용자명"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        {error && <div className="error">{error}</div>}
        <button type="submit" disabled={loading}>
          {loading ? '로그인 중...' : '로그인'}
        </button>
      </form>
    </div>
  );
};

export default AdminLogin;
