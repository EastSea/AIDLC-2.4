import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  Container, 
  Typography, 
  Button, 
  Box,
  Paper,
  AppBar,
  Toolbar,
  IconButton,
  Chip,
  Divider
} from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import { getMenuDetail } from '../../services/menuService';
import { useCart } from '../../hooks/useCart';
import { useAuth } from '../../hooks/useAuth';
import StaffCallButton from './StaffCallButton';

const PageWrapper = styled.div`
  min-height: 100vh;
  background-color: #f5f5f5;
  padding-bottom: 100px;
`;

const MenuImage = styled.img`
  width: 100%;
  height: 400px;
  object-fit: cover;
`;

const ContentSection = styled(Paper)`
  margin-top: -50px;
  border-radius: 20px 20px 0 0;
  padding: 32px;
  position: relative;
`;

const PriceText = styled(Typography)`
  color: #e91e63;
  font-weight: bold;
  font-size: 28px;
`;

const BottomBar = styled(Box)`
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: white;
  padding: 16px 24px;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
  display: flex;
  gap: 16px;
`;

const MenuDetail = () => {
  const { menuId } = useParams();
  const [menu, setMenu] = useState(null);
  const [loading, setLoading] = useState(true);
  const { addItem } = useCart();
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    fetchMenuDetail();
  }, [menuId]);

  const fetchMenuDetail = async () => {
    try {
      const data = await getMenuDetail(menuId);
      setMenu(data);
    } catch (err) {
      console.error('Failed to fetch menu detail:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddToCart = () => {
    addItem(menu);
    navigate('/');
  };

  if (loading) {
    return (
      <PageWrapper>
        <AppBar position="fixed" sx={{ backgroundColor: '#333' }}>
          <Toolbar>
            <IconButton edge="start" color="inherit" onClick={() => navigate('/')}>
              <ArrowBackIcon />
            </IconButton>
            <Typography variant="h6" sx={{ flexGrow: 1 }}>
              메뉴 상세
            </Typography>
          </Toolbar>
        </AppBar>
        <Container sx={{ mt: 10 }}>
          <Typography>로딩 중...</Typography>
        </Container>
      </PageWrapper>
    );
  }

  if (!menu) {
    return (
      <PageWrapper>
        <AppBar position="fixed" sx={{ backgroundColor: '#333' }}>
          <Toolbar>
            <IconButton edge="start" color="inherit" onClick={() => navigate('/')}>
              <ArrowBackIcon />
            </IconButton>
            <Typography variant="h6" sx={{ flexGrow: 1 }}>
              메뉴 상세
            </Typography>
          </Toolbar>
        </AppBar>
        <Container sx={{ mt: 10 }}>
          <Typography>메뉴를 찾을 수 없습니다</Typography>
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
            메뉴 상세
          </Typography>
          {user?.tableId && <StaffCallButton tableId={user.tableId} />}
        </Toolbar>
      </AppBar>

      <Box sx={{ mt: 8 }}>
        <MenuImage 
          src={menu.image_url || 'https://via.placeholder.com/800x400?text=No+Image'} 
          alt={menu.name} 
        />
        
        <ContentSection elevation={3}>
          <Typography variant="h4" gutterBottom>
            {menu.name}
          </Typography>
          
          {menu.serving_size && menu.serving_size !== 'all' && (
            <Chip 
              label={menu.serving_size} 
              color="primary"
              sx={{ mb: 2 }}
            />
          )}
          
          <PriceText gutterBottom>
            {menu.price.toLocaleString()}원
          </PriceText>
          
          <Divider sx={{ my: 3 }} />
          
          <Typography variant="h6" gutterBottom>
            메뉴 설명
          </Typography>
          <Typography variant="body1" color="text.secondary" paragraph>
            {menu.description || '메뉴 설명이 없습니다.'}
          </Typography>
          
          {menu.is_available === false && (
            <Box sx={{ mt: 2, p: 2, backgroundColor: '#ffebee', borderRadius: 1 }}>
              <Typography color="error">
                현재 품절된 메뉴입니다
              </Typography>
            </Box>
          )}
        </ContentSection>
      </Box>

      <BottomBar>
        <Button 
          variant="outlined" 
          size="large"
          fullWidth
          onClick={() => navigate('/')}
        >
          메뉴 더보기
        </Button>
        <Button 
          variant="contained" 
          color="primary"
          size="large"
          fullWidth
          startIcon={<AddShoppingCartIcon />}
          onClick={handleAddToCart}
          disabled={menu.is_available === false}
        >
          장바구니 담기
        </Button>
      </BottomBar>
    </PageWrapper>
  );
};

export default MenuDetail;
