import React from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';
import { 
  Container, 
  Typography, 
  Button, 
  Box,
  Card,
  CardContent,
  IconButton,
  AppBar,
  Toolbar,
  Divider
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { useCart } from '../../hooks/useCart';
import { useAuth } from '../../hooks/useAuth';
import { createOrder } from '../../services/orderService';
import StaffCallButton from './StaffCallButton';

const PageWrapper = styled.div`
  min-height: 100vh;
  background-color: #f5f5f5;
  padding-bottom: 100px;
`;

const CartItem = styled(Card)`
  margin-bottom: 16px;
`;

const QuantityControl = styled(Box)`
  display: flex;
  align-items: center;
  gap: 8px;
`;

const TotalSection = styled(Box)`
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: white;
  padding: 24px;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
`;

const Cart = () => {
  const { items, updateQuantity, removeItem, clearCart, totalAmount } = useCart();
  const { user } = useAuth();
  const navigate = useNavigate();

  const handleCheckout = async () => {
    if (!user?.sessionId) {
      alert('로그인이 필요합니다');
      navigate('/login');
      return;
    }

    try {
      const orderItems = items.map((item) => ({
        menuId: item.id,
        quantity: item.quantity,
      }));
      
      await createOrder(user.sessionId, orderItems);
      clearCart();
      alert('주문이 완료되었습니다');
      navigate('/orders');
    } catch (err) {
      alert('주문 실패: ' + (err.response?.data?.message || err.message));
    }
  };

  if (items.length === 0) {
    return (
      <PageWrapper>
        <AppBar position="fixed" sx={{ backgroundColor: '#333' }}>
          <Toolbar>
            <IconButton edge="start" color="inherit" onClick={() => navigate('/')}>
              <ArrowBackIcon />
            </IconButton>
            <Typography variant="h6" sx={{ flexGrow: 1 }}>
              장바구니
            </Typography>
            {user?.tableId && <StaffCallButton tableId={user.tableId} />}
          </Toolbar>
        </AppBar>
        <Container sx={{ mt: 10, textAlign: 'center' }}>
          <Typography variant="h6" color="text.secondary">
            장바구니가 비어있습니다
          </Typography>
          <Button 
            variant="contained" 
            sx={{ mt: 2 }}
            onClick={() => navigate('/')}
          >
            메뉴 보러가기
          </Button>
        </Container>
      </PageWrapper>
    );
  }

  return (
    <PageWrapper>
      <AppBar position="fixed" sx={{ backgroundColor: '#333' }}>
        <Toolbar>
          <IconButton edge="start" color="inherit" onClick={() => navigate('/')}>
            <ArrowBackIcon />
          </IconButton>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            장바구니
          </Typography>
          {user?.tableId && <StaffCallButton tableId={user.tableId} />}
        </Toolbar>
      </AppBar>

      <Container sx={{ mt: 10 }}>
        {items.map((item) => (
          <CartItem key={item.id}>
            <CardContent>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <Box sx={{ flex: 1 }}>
                  <Typography variant="h6" gutterBottom>
                    {item.name}
                  </Typography>
                  <Typography variant="body2" color="text.secondary" gutterBottom>
                    {item.price.toLocaleString()}원
                  </Typography>
                  <QuantityControl>
                    <IconButton 
                      size="small" 
                      onClick={() => updateQuantity(item.id, item.quantity - 1)}
                    >
                      <RemoveIcon />
                    </IconButton>
                    <Typography variant="body1" sx={{ minWidth: 30, textAlign: 'center' }}>
                      {item.quantity}
                    </Typography>
                    <IconButton 
                      size="small"
                      onClick={() => updateQuantity(item.id, item.quantity + 1)}
                    >
                      <AddIcon />
                    </IconButton>
                  </QuantityControl>
                </Box>
                <Box sx={{ textAlign: 'right' }}>
                  <Typography variant="h6" color="primary" gutterBottom>
                    {(item.price * item.quantity).toLocaleString()}원
                  </Typography>
                  <IconButton 
                    color="error" 
                    onClick={() => removeItem(item.id)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </Box>
              </Box>
            </CardContent>
          </CartItem>
        ))}
      </Container>

      <TotalSection>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
          <Typography variant="h6">총 금액</Typography>
          <Typography variant="h5" color="primary">
            {totalAmount.toLocaleString()}원
          </Typography>
        </Box>
        <Button 
          variant="contained" 
          color="error"
          fullWidth
          size="large"
          onClick={handleCheckout}
        >
          주문하기
        </Button>
      </TotalSection>
    </PageWrapper>
  );
};

export default Cart;
