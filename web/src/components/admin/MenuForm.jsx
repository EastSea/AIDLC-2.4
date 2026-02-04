import React, { useState, useEffect } from 'react';
import { createMenu, updateMenu } from '../../services/adminMenuService';

/**
 * Menu form component
 * @param {Object} props
 * @param {Object} [props.menu] - Menu data for editing
 * @param {Function} props.onSubmit - Submit callback
 * @param {Function} props.onCancel - Cancel callback
 */
const MenuForm = ({ menu, onSubmit, onCancel }) => {
  const [formData, setFormData] = useState({
    categoryId: '',
    name: '',
    price: '',
    description: '',
    servingSize: '',
    imageUrl: '',
  });
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (menu) {
      setFormData(menu);
    }
  }, [menu]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      if (menu) {
        await updateMenu(menu.id, formData);
      } else {
        await createMenu(formData);
      }
      onSubmit();
    } catch (err) {
      alert('저장 실패: ' + (err.response?.data?.message || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="menu-form">
      <h3>{menu ? '메뉴 수정' : '새 메뉴 추가'}</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="categoryId"
          placeholder="카테고리 ID"
          value={formData.categoryId}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="name"
          placeholder="메뉴명"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="price"
          placeholder="가격"
          value={formData.price}
          onChange={handleChange}
          required
        />
        <textarea
          name="description"
          placeholder="설명"
          value={formData.description}
          onChange={handleChange}
        />
        <input
          type="text"
          name="servingSize"
          placeholder="인원 (예: 2인분)"
          value={formData.servingSize}
          onChange={handleChange}
        />
        <input
          type="text"
          name="imageUrl"
          placeholder="이미지 URL"
          value={formData.imageUrl}
          onChange={handleChange}
        />
        <div className="form-actions">
          <button type="submit" disabled={loading}>
            {loading ? '저장 중...' : '저장'}
          </button>
          <button type="button" onClick={onCancel}>
            취소
          </button>
        </div>
      </form>
    </div>
  );
};

export default MenuForm;
