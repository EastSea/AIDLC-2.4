import React, { useState, useEffect } from "react";
import styled from "styled-components";
import {
  Container,
  Grid,
  Card,
  CardMedia,
  CardContent,
  Typography,
  Button,
  Box,
  Chip,
  AppBar,
  Toolbar,
  IconButton,
  Badge,
} from "@mui/material";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import RestaurantIcon from "@mui/icons-material/Restaurant";
import { getCategories, getMenus } from "../../services/menuService";
import { useCart } from "../../hooks/useCart";
import { useAuth } from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";
import StaffCallButton from "./StaffCallButton";

const PageWrapper = styled.div`
  min-height: 100vh;
  background-color: #f5f5f5;
`;

const Sidebar = styled.div`
  position: fixed;
  left: 0;
  top: 64px;
  width: 200px;
  height: calc(100vh - 64px);
  background-color: white;
  border-right: 1px solid #e0e0e0;
  overflow-y: auto;
`;

const CategoryButton = styled(Button)`
  width: 100%;
  justify-content: flex-start;
  padding: 16px 24px;
  text-transform: none;
  font-size: 16px;
  color: ${(props) => (props.active ? "white" : "#333")};
  background-color: ${(props) => (props.active ? "#e91e63" : "transparent")};

  &:hover {
    background-color: ${(props) => (props.active ? "#c2185b" : "#f5f5f5")};
  }
`;

const MainContent = styled.div`
  margin-left: 200px;
  padding: 24px;
`;

const MenuGrid = styled(Grid)`
  margin-top: 16px;
`;

const MenuCard = styled(Card)`
  cursor: pointer;
  transition: transform 0.2s;
  height: 420px;
  width: 200px;
  max-width: 100%;
  display: flex;
  flex-direction: column;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  }

  .MuiCardMedia-root {
    height: 200px;
    flex-shrink: 0;
    object-fit: cover;
    background: linear-gradient(135deg, #ffd6e8 0%, #c5e3ff 100%);
  }

  .MuiCardContent-root {
    height: 220px;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    padding: 16px;
    overflow: hidden;
  }
`;

const PriceText = styled(Typography)`
  color: #e91e63;
  font-weight: bold;
  font-size: 18px;
`;

const BottomBar = styled(Box)`
  position: fixed;
  bottom: 0;
  left: 200px;
  right: 0;
  background-color: #333;
  color: white;
  padding: 16px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1000;
`;

const MenuBrowser = () => {
  const [categories, setCategories] = useState([]);
  const [menus, setMenus] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("all");
  const [loading, setLoading] = useState(false);

  const { items, addItem, totalAmount } = useCart();
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    fetchCategories();
    fetchMenus();
  }, []);

  useEffect(() => {
    fetchMenus();
  }, [selectedCategory]);

  const fetchCategories = async () => {
    try {
      const data = await getCategories();
      setCategories(data);
    } catch (err) {
      console.error("Failed to fetch categories:", err);
    }
  };

  const fetchMenus = async () => {
    setLoading(true);
    try {
      const categoryId = selectedCategory === "all" ? null : selectedCategory;
      const data = await getMenus(categoryId, null);
      setMenus(data);
    } catch (err) {
      console.error("Failed to fetch menus:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddToCart = (menu) => {
    addItem(menu);
  };

  return (
    <PageWrapper>
      <AppBar position="fixed" sx={{ backgroundColor: "#333" }}>
        <Toolbar>
          <RestaurantIcon sx={{ mr: 2 }} />
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            POS
          </Typography>
          {user?.tableId && <StaffCallButton tableId={user.tableId} />}
          <IconButton color="inherit" onClick={() => navigate("/cart")}>
            <Badge badgeContent={items.length} color="error">
              <ShoppingCartIcon />
            </Badge>
          </IconButton>
        </Toolbar>
      </AppBar>

      <Sidebar>
        <CategoryButton
          active={selectedCategory === "all" ? 1 : 0}
          onClick={() => setSelectedCategory("all")}
        >
          전체메뉴
        </CategoryButton>
        {categories.map((cat) => (
          <CategoryButton
            key={cat.id}
            active={selectedCategory === cat.id ? 1 : 0}
            onClick={() => setSelectedCategory(cat.id)}
          >
            {cat.name}
          </CategoryButton>
        ))}
      </Sidebar>

      <MainContent>
        <Box sx={{ mt: 8 }}>
          <Typography variant="h5" gutterBottom>
            {selectedCategory === "all"
              ? "전체메뉴"
              : categories.find((c) => c.id === selectedCategory)?.name ||
                "메뉴"}
          </Typography>

          {loading ? (
            <Typography>로딩 중...</Typography>
          ) : (
            <MenuGrid container spacing={3}>
              {menus.map((menu) => (
                <Grid item xs={12} sm={6} md={4} lg={3} key={menu.id} sx={{ display: 'flex' }}>
                  <MenuCard onClick={() => navigate(`/menu/${menu.id}`)}>
                    <CardMedia
                      component="div"
                      sx={{
                        height: 200,
                        background: menu.image_url 
                          ? `url(${menu.image_url}) center/cover`
                          : 'linear-gradient(135deg, #ffd6e8 0%, #c5e3ff 100%)'
                      }}
                    />
                    <CardContent>
                      <Typography
                        variant="h6"
                        sx={{
                          overflow: "hidden",
                          textOverflow: "ellipsis",
                          display: "-webkit-box",
                          WebkitLineClamp: 2,
                          WebkitBoxOrient: "vertical",
                          height: "3.6em",
                          mb: 1
                        }}
                      >
                        {menu.name}
                      </Typography>
                      <Typography
                        variant="body2"
                        color="text.secondary"
                        sx={{
                          overflow: "hidden",
                          textOverflow: "ellipsis",
                          display: "-webkit-box",
                          WebkitLineClamp: 2,
                          WebkitBoxOrient: "vertical",
                          height: "2.8em",
                          mb: 1
                        }}
                      >
                        {menu.description}
                      </Typography>
                      {menu.serving_size && menu.serving_size !== "all" && (
                        <Chip
                          label={menu.serving_size}
                          size="small"
                          sx={{ mb: 1, alignSelf: "flex-start" }}
                        />
                      )}
                      <Box
                        sx={{
                          display: "flex",
                          justifyContent: "space-between",
                          alignItems: "center",
                          mt: "auto"
                        }}
                      >
                        <PriceText>{menu.price.toLocaleString()}원</PriceText>
                        <Button
                          variant="contained"
                          color="primary"
                          size="small"
                          onClick={(e) => {
                            e.stopPropagation();
                            handleAddToCart(menu);
                          }}
                        >
                          담기
                        </Button>
                      </Box>
                    </CardContent>
                  </MenuCard>
                </Grid>
              ))}
            </MenuGrid>
          )}
        </Box>
      </MainContent>

      {items.length > 0 && (
        <BottomBar>
          <Box>
            <Typography variant="body2">장바구니</Typography>
            <Typography variant="h6">
              {totalAmount.toLocaleString()}원
            </Typography>
          </Box>
          <Button
            variant="contained"
            color="error"
            size="large"
            onClick={() => navigate("/cart")}
          >
            주문하기 ({items.length})
          </Button>
        </BottomBar>
      )}
    </PageWrapper>
  );
};

export default MenuBrowser;
