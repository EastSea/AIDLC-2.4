import React, { useState } from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';
import { 
  Container, 
  TextField, 
  Button, 
  Typography, 
  Box,
  Paper,
  Alert
} from '@mui/material';
import RestaurantIcon from '@mui/icons-material/Restaurant';
import { loginTable } from '../../services/authService';
import { useAuth } from '../../hooks/useAuth';

const PageWrapper = styled.div`
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
`;

const LoginCard = styled(Paper)`
  padding: 48px;
  max-width: 400px;
  width: 100%;
`;

const Logo = styled(Box)`
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 32px;
  color: #667eea;
`;

const CustomerLogin = () => {
  const [storeCode, setStoreCode] = useState('');
  const [tableNumber, setTableNumber] = useState('');
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
      const data = await loginTable(storeCode, parseInt(tableNumber), password);
      login({ 
        token: data.token,
        tableId: data.table_id, 
        sessionId: data.session_id,
        tableNumber: parseInt(tableNumber) 
      }, 'table');
      navigate('/');
    } catch (err) {
      setError(err.response?.data?.message || '로그인 실패');
    } finally {
      setLoading(false);
    }
  };

  return (
    <PageWrapper>
      <Container maxWidth="sm">
        <LoginCard elevation={3}>
          <Logo>
            <RestaurantIcon sx={{ fontSize: 48, mr: 2 }} />
            <Typography variant="h4" component="h1">
              EOS POS
            </Typography>
          </Logo>
          
          <Typography variant="h5" align="center" gutterBottom>
            테이블 로그인
          </Typography>
          
          <Box component="form" onSubmit={handleLogin} sx={{ mt: 3 }}>
            <TextField
              fullWidth
              label="매장 코드"
              value={storeCode}
              onChange={(e) => setStoreCode(e.target.value)}
              margin="normal"
              required
            />
            <TextField
              fullWidth
              type="number"
              label="테이블 번호"
              value={tableNumber}
              onChange={(e) => setTableNumber(e.target.value)}
              margin="normal"
              required
            />
            <TextField
              fullWidth
              type="password"
              label="비밀번호"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              margin="normal"
              required
            />
            
            {error && (
              <Alert severity="error" sx={{ mt: 2 }}>
                {error}
              </Alert>
            )}
            
            <Button
              type="submit"
              fullWidth
              variant="contained"
              size="large"
              disabled={loading}
              sx={{ mt: 3, mb: 2 }}
            >
              {loading ? '로그인 중...' : '로그인'}
            </Button>
          </Box>
        </LoginCard>
      </Container>
    </PageWrapper>
  );
};

export default CustomerLogin;
