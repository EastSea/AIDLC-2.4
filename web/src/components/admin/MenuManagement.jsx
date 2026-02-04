import React, { useEffect, useState } from 'react';
import { getAdminMenus, deleteMenu } from '../../services/adminMenuService';
import MenuForm from './MenuForm';

/**
 * Menu management component
 */
const MenuManagement = () => {
  const [menus, setMenus] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingMenu, setEditingMenu] = useState(null);
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    fetchMenus();
  }, []);

  const fetchMenus = async () => {
    try {
      const data = await getAdminMenus();
      setMenus(data);
    } catch (err) {
      console.error('Failed to fetch menus:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingMenu(null);
    setShowForm(true);
  };

  const handleEdit = (menu) => {
    setEditingMenu(menu);
    setShowForm(true);
  };

  const handleDelete = async (menuId) => {
    if (!window.confirm('정말 삭제하시겠습니까?')) return;

    try {
      await deleteMenu(menuId);
      setMenus((prev) => prev.filter((menu) => menu.id !== menuId));
    } catch (err) {
      alert('삭제 실패: ' + (err.response?.data?.message || err.message));
    }
  };

  const handleFormSubmit = () => {
    setShowForm(false);
    setEditingMenu(null);
    fetchMenus();
  };

  if (loading) return <div>로딩 중...</div>;

  return (
    <div className="menu-management">
      <h2>메뉴 관리</h2>
      
      <button onClick={handleCreate}>새 메뉴 추가</button>

      {showForm && (
        <MenuForm
          menu={editingMenu}
          onSubmit={handleFormSubmit}
          onCancel={() => setShowForm(false)}
        />
      )}

      <div className="menu-list">
        {menus.map((menu) => (
          <div key={menu.id} className="menu-item">
            <h3>{menu.name}</h3>
            <p>{menu.price.toLocaleString()}원</p>
            <p>{menu.servingSize}</p>
            <button onClick={() => handleEdit(menu)}>수정</button>
            <button onClick={() => handleDelete(menu.id)}>삭제</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MenuManagement;
